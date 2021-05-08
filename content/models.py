from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

class Menu(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False','Hayır'),
    )

    parent = TreeForeignKey('self', blank=True, null = True, related_name="children",on_delete=models.CASCADE)
    #content models.OneToOnteRel(Content, blank= True, )
    title = models.CharField(max_length=100,unique=True)
    link = models.CharField(max_length=100,blank=True)
    status = models.CharField(max_length=10,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']
    
    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k=k.parent
        return ' / '.join(full_path[::-1])

class Content(models.Model):
    TYPE = (
        ('menu', 'menü'),
        ('haber','haber'),
        ('duyuru','duyuru'),
        ('etkinlik','etkinlik')
    )
    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )

    menu = models.OneToOneField(Menu, null=True, blank=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE)
    title = models.CharField(max_length=150)
    keywords = models.CharField(blank=True,max_length=255)
    description = models.CharField(blank=True,max_length=255)
    image = models.ImageField(blank=True, null=True,upload_to='images/')
    detail = RichTextUploadingField()
    slug = models.SlugField(null=False, unique=True)
    status = models.CharField(max_length=10,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
        else:
            return "Resim Yüklü Değil"

    def get_absolute_url(self):
        return reverse('content_detail',kwargs={'slug':self.slug})


class CImages(models.Model):
    content = models.ForeignKey(Content,on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image=models.ImageField(blank=True,upload_to='images/')
    def __str__(self):
        return self.title 
    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
        else:
            return "Resim Yüklü Değil"
    image_tag.short_description = 'Image'