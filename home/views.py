from django.shortcuts import render,redirect
from .models import Setting,ContactForm,ContactFormMessage,UserProfile
from product.models import Product
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout,authenticate,login
from .form import SignUpForm
from django.http import HttpResponse,HttpResponseRedirect
from order.models import ShopCart
from content.models import Content, Menu, CImages
def Index(request):
    current_user=request.user
    settings=Setting.objects.get(id=1)
    sliderdata = Product.objects.all()[:4]
    request.session['cart_items'] = ShopCart.objects.filter(user_id= current_user.id).count()
    menu = Menu.objects.all()  # E ticaret dışı
    news = Content.objects.filter(type='haber').order_by('-id')[:2]  # E ticaret dışı
    announcement=  Content.objects.filter(type='duyuru').order_by('-id')[:2]  # E ticaret dışı
    context = {
        'settings':settings, 'sliderdata':sliderdata,'news':news,'announcement':announcement, 'page': 'home', 'menu':menu
    }
    return render(request,'home/home.html',context)
def aboutus(request):
    settings=Setting.objects.get(id=1)
    context = {
        'settings':settings,
    }
    return render(request,'home/aboutus.html',context)
  
def reference(request):
    settings=Setting.objects.get(id=1)
    context = {
        'settings':settings,
    }
    return render(request,'home/reference.html',context)

def contact(request):
   if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage() #create relation with model
            data.name = form.cleaned_data['name'] # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.save()  #save data to table
            # messages.success(request,"Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/contact')
   else:      
        form = ContactForm
        settings=Setting.objects.get(id=1)
        context={'settings':settings,'form':form  }
        return render(request, 'home/contact.html', context)   

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password  = request.POST['password']

        user = auth.authenticate(username= username, password = password)
        if user is not None:
            auth.login(request, user)
            # messages.add_message(request, messages.SUCCESS,'Oturum açıldı.')
            return redirect('/')
        else:
            # messages.add_message(request, messages.SUCCESS, 'Hatalı username yada parola')
            return redirect('login')
    else:
       
        settings=Setting.objects.get(id=1)
        context={'settings':settings }
        return render(request, 'home/login.html', context)
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():           
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user =request.user
            # return HttpResponse("Üye Kaydedildi.")
            data=UserProfile()
            data.user_id=current_user.id
            data.image="images/users/admin.png"
            data.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse(form.errors)
    form = SignUpForm()
    settings=Setting.objects.get(id=1)
    context={'settings':settings, 'form': form }
    return render(request, 'home/signup.html',context)
# Eticaret dışı
def menu(request,id):
    content=Content.objects.get(menu_id = id)
    if content:
        link =  'content/'+ str(content.d)       
        return HttpResponseRedirect(link)
    else:
        link ='/'
        return HttpResponseRedirect(link)

def contentdetail(request,id,slug):
    menu= Menu.objects.all()
    content= Content.objects.get(pk=id)
    images = CImages.objects.filter(content_id= id)
    context = {
        'menu':menu, 'content':content, 'images':images
    }
    return render(request,'content_detail.html',context)


# Content olan haber, içerik ve yorum...
