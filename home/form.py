from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput
class SignUpForm(UserCreationForm): 
    username = forms.CharField(widget=forms.TextInput(attrs = {'class': 'form-control',}),max_length=30,label= 'User Name :')
    email = forms.EmailField(widget=forms.TextInput(attrs = {'class': 'form-control',}),max_length=200,label= 'Email :')
    first_name = forms.CharField(widget=forms.TextInput(attrs = {'class': 'form-control',}),max_length=100, help_text='First Name',label= 'İsminizi Girin: :')
    last_name = forms.CharField(widget=forms.TextInput(attrs = {'class': 'form-control',}),max_length=100, help_text='Last Name',label= 'Soyisminizi Girin:')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs = {'class': 'form-control',}),max_length=100,label="Şifrenizi Giriniz")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs = {'class': 'form-control',}),max_length=100, label="Şifreyi Tekrar Giriniz")
    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1', 'password2', )
   

# class SignUpForm(UserCreationForm):
#     username = forms.CharField(max_length=30,label= 'User Name :')
#     email = forms.EmailField(max_length=200,label= 'Email :')
#     first_name = forms.CharField(max_length=100, help_text='First Name',label= 'First Name :')
#     last_name = forms.CharField(max_length=100, help_text='Last Name',label= 'First Name :')

#     class Meta:
#         model = User
#         fields = ('username', 'email','first_name','last_name', 'password1', 'password2', )
# Parolanız diğer kişisel bilgileriniz ile çok benzer olamaz.
# Parolanız en az 8 karakter içermek zorundadır.
# Parolanız yaygın olarak kullanılan bir parola olamaz.
# Parolanız tamamıyla sayısal olamaz.