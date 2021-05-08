from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ShopCart,ShopCartForm,OrderForm,Order,OrderProduct
from home.models import UserProfile,Setting
from product.models import Product
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    return HttpResponse('Order App')

@login_required(login_url='/login')# loginKontrolü için
def addtocart(request,id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checkcontrol = ShopCart.objects.filter(product_id=id) # Ürün Sepette Varmı Filtreleme
    if checkcontrol:
        control = 1 # Ürün Sepette Var
    else:
        control = 0  # Ürün Sepette Yok
    if request.method == 'POST': # Ürün detail sayfasından Geldi İse(Detay İşlemleri İçin)
        form=ShopCartForm(request.POST)
        
        #****** ÜRÜN SEPETTE VAR MI KONTROLÜ   ********#         
        if form.is_valid():
            if control==1: # Olan Ürünün Üzerine Ekle  
                data = ShopCart.objects.get(product_id=id)                            
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:#Bu Üründen Hiç Yoksa Ekle
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()   
            request.session['cart_items'] = ShopCart.objects.filter(user_id= current_user.id).count()
            #Ürün Başarı İle Sepete Eklenmiştir. Teşekkür Ederiz
            return HttpResponseRedirect(url)                   
    else:  # İstek Direk Olarak Ürün Ekle Butonuna Basılarak Geldi İse(Listeden Sepete Ekleme İşlemleri İçin )
        if control==1: # Olan Ürünün Üzerine Ekle
            data = ShopCart.objects.get(product_id=id) 
            data.quantity += 1
            data.save()
        
        else:# Ürün Yoksa Ekle           
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()# veri tabanına kaydet
            # Ürün Başarı İle Sepete Eklenmiştir. Teşekkür Ederiz.
        request.session['cart_items'] = ShopCart.objects.filter(user_id= current_user.id).count()
        return HttpResponseRedirect(url)
    
    # Ürün Eklemede Hata Oluştu.   
    return HttpResponseRedirect(url)           
@login_required(login_url='/login') 
def deletetocart(request,id):
    current_user = request.user
    ShopCart.objects.filter(id=id).delete()
    request.session['cart_items'] = ShopCart.objects.filter(user_id= current_user.id).count()
    return HttpResponseRedirect("/order/shopcart")
def shopcart(request):
    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    request.session['cart_items'] = ShopCart.objects.filter(user_id= current_user.id).count()
    total=0
    for rs in shopcart:
        total += rs.product.price * rs.quantity
    #return HttpResponse(str(total))
    context={'shopcart': shopcart,
             'total': total,
             }
    return render(request,'order/shoppingcart.html',context)


@login_required(login_url='/login')
def orderproduct(request):
    current_user = request.user # Talebin User Nesnesini current_userda tuttuk 
    shopcart = ShopCart.objects.filter(user_id=current_user.id) # Gelen current_user.id yi user_id ye aldık
    total = 0  
    for rs in shopcart:   
        total += rs.product.price * rs.quantity # total fiyat hesabı yapıldı

    if request.method == 'POST':  # Eğer Formdan Gönderildi ise Oldu İse
        form = OrderForm(request.POST)
        #return HttpResponse(request.POST.items())
        if form.is_valid():
            # Send Credit card to bank,  If the bank responds ok, continue, if not, show the error
            # ..............

            data = Order()
            data.first_name = form.cleaned_data['first_name'] #Ürün adeti getir formdan
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode= get_random_string(5).upper() # Rasgele Kod Üretildi.
            data.code =  ordercode
            data.save() # Veritabanı Kaydı Yapıldı.

            shopcart=ShopCart.objects.filter(user_id=current_user.id)
            for rs in shopcart:
                detail = OrderProduct()
                detail.order_id     = data.id # Order Id
                detail.product_id   = rs.product_id
                detail.user_id      = current_user.id
                detail.quantity     = rs.quantity
                detail.price    = rs.product.price
                detail.amount   = rs.amount         
                detail.save()
                ## Reduce quantity of sold product from Amount of Product  Stocktan Düşme
                product = Product.objects.get(id=rs.product_id)
                product.amount -= rs.quantity
                product.save() # ürün sayısı kaydedildi.
                #*************<>***************#


            ShopCart.objects.filter(user_id=current_user.id).delete() # Sepeti Temizle
            request.session['cart_items']=0  # Ürün Sayısını Sıfırla
            # messages.success(request, "Your Order has been completed. Thank you ")
            return render(request, 'order/order_completed.html',{'ordercode':ordercode})
        else:
            # messages.warning(request, form.errors) 
            return HttpResponse(form.errors)
            # return HttpResponseRedirect("/order/orderproduct")

    form= OrderForm()
    settings = Setting.objects.get(pk=1)
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {
               'settings':settings,
                'shopcart': shopcart,
               'total': total,
               'form': form,
               'profile': profile,
               }
    return render(request, 'order/order_form.html', context)