from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.models import UserProfile,Setting
from product.models import Comment
from order.models import Order, OrderProduct
from .forms import UserUpdateForm,ProfileUpdateForm
# Create your views here.
def index(request):
    
    current_user = request.user  
    profile = UserProfile.objects.get(user_id=current_user.id)
    settings = Setting.objects.get(pk=1)
    context = {
               'settings':settings,
               'profile':profile,

               
               }
    return render(request,'user/user_profile.html',context)

@login_required(login_url='/login') # Check login
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user  data
        # instance=request.user.userprofile bize userprofile user teke teke ilişkisi için lazım 
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
         #   messages.success(request, 'Your account has been updated!')
          #  return HttpResponse('Sistem Başarılı Oldu.')
            return HttpResponseRedirect('/user/user-profile')
        else:
            return HttpResponse('Form Hatalı Oldu')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile) #"userprofile" model -> OneToOneField relatinon with user
        context = {
            
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user/user_update.html', context)
        # Post Olmadığı İçin
@login_required(login_url='/login') 
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Önemli!
            # messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user/user-profile')
        else:
            # messages.error(request, 'Please correct the error below.<br>'+ str(form.errors))
            # return HttpResponseRedirect('/user/password')
            return HttpResponse('Form Hatalı Oldu')
    else:
        # Post Olmadı İse:
        form = PasswordChangeForm(request.user)
        return render(request, 'user/user_password.html', {'form': form,#'category': category
                       })

@login_required(login_url='/login') # Check login
def user_orders(request):
    #category = Category.objects.all()
    current_user = request.user
    orders=Order.objects.filter(user_id=current_user.id)
    user = current_user
    context = {#'category': category,
               'orders': orders,
               'user':user
               }
    return render(request, 'user/user_orders.html', context)

@login_required(login_url='/login') # Check login
def user_orderdetail(request,id):
    #category = Category.objects.all()
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=id)
    orderitems = OrderProduct.objects.filter(order_id=id)
    context = {
        #'category': category,
        'order': order,
        'orderitems': orderitems,
    }
    return render(request, 'user/user_order_detail.html', context)
@login_required(login_url='/login') # Check login
def user_comments(request):
    # return HttpResponse('Yorumlar')
     #category = Category.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {
        #'category': category,
        'comments': comments,
    }
    return render(request, 'user/user_comments.html', context)


@login_required(login_url='/login') # Check login
def user_deletecomment(request,id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    # messages.success(request, 'Comment deleted..')
    return HttpResponseRedirect('/user/comments')