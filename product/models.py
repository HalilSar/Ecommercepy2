from django.db import  models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
class Category(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    parent = TreeForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10, choices=STATUS,default="True")
    slug = models.SlugField(null=False,unique=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['title']
    def __str__(self):
        full_path= [self.title]
        k=self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '/'.join(full_path[::-1])
    def get_image_path(self):
        return '/images/'+ self.image
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})
class Product(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE) #many to one relation with Category
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/',null=False)
    price = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    amount=models.IntegerField(default=0)
    minamount=models.IntegerField(default=3)   
    detail=RichTextUploadingField()
    slug = models.SlugField(null=False,unique=True)
    status=models.CharField(max_length=10,choices=STATUS,default="True")
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
      return self.title
    def get_image_path(self):
        return '/images/'+ self.image
            
    def image_tag(self):

        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
        else:
            return "Resim Yüklü Değil"
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug}) 
    image_tag.short_description = 'Image'
class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image=models.ImageField(blank=True,upload_to='images/',null=False)
    def __str__(self):
        return self.title 
  
class Comment(models.Model):
    STATUS = ( 
        ('New','Yeni'),
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    comment = models.CharField(max_length=250,blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']

