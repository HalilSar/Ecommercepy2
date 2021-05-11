from django.db import models
from django import forms
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True,max_length=100)
    phone = models.CharField(blank=True,max_length=15)
    fax = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    smtpserver = models.CharField(blank=True,max_length=50)
    smtpemail = models.CharField(blank=True,max_length=50)
    smtppassword = models.CharField(blank=True,max_length=10)
    smtpport = models.CharField(blank=True,max_length=5)
    icon = models.ImageField(blank=True,upload_to='images/')
    facebook = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    aboutus = RichTextUploadingField(blank=True)
    contact =  RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactFormMessage(models.Model):

    STATUS = (
        ('New', 'Yeni'),
        ('Read', 'Okundu'),
        
    )
    name= models.CharField(blank=True,max_length=20)
    email= models.CharField(blank=True,max_length=50)
    subject= models.CharField(blank=True,max_length=50)
    message= models.TextField(blank=True,max_length=255)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs = {'class': 'form-control input-lg','placeholder':'İsminiz*'}),max_length=100,label= 'İsminizi Girin: :')
    phone = forms.CharField(widget=forms.TextInput(attrs = {'class': 'form-control input-lg','placeholder':'Telefon'}),max_length=100,label= 'Telefonunuzu Girin: :')
    subject = forms.CharField(widget=forms.TextInput(attrs = {'class': 'form-control input-lg','placeholder':'Konu'}),max_length=100,label= 'Konuyu Girin: :')
    email = forms.CharField(widget=forms.TextInput(attrs = {'class': 'form-control input-lg','placeholder':'Email Adresiniz'}),max_length=100,label= 'Email Girin: :')
    message = forms.CharField(widget=forms.Textarea(attrs = {'class': 'form-control input-lg','placeholder':'Mesajınız*','rows':'12'}),max_length=100,label= 'İsminizi Girin: :')
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email','phone', 'subject','message']
      
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True, upload_to='images/users/')

    # User bilgisini admin gösterme
    def __str__(self):
        return self.user.username
    
    def user_name(self):
        return self.user.first_name +' ' + self.user.last_name
    
    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" height="50"/>')
    image_tag.short_description = 'Image'  
           
        
            
    
    
    


    

class UserForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address','address',  'city','image']
        