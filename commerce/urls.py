"""commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from home import views
from product import views as productviews
from order import views as orderviews
urlpatterns = [ 
    path('',include('home.urls')),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contact/',views.contact,name='contact'),
    path('reference/',views.reference,name='reference'),
    path('product/', include('product.urls')),
    path('user/', include('user.urls')),
    path('content/',include('content.urls')),
    path('order/',include('order.urls')),
    path('menu/<int:id>', views.menu ,name="menu"),
    path('order/addtocart/<int:id>',orderviews.addtocart,name="addtocart"),
    path('order/shopcart/',orderviews.shopcart,name="shopcart"),
    path('order/deletetocart/<int:id>',orderviews.deletetocart, name="deletetocart"),
    path('order/orderproduct/',orderviews.orderproduct, name="orderproduct"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('login/', views.login_view,name="login"),
    path('admin/', admin.site.urls),
    path('category/<int:category_id>/<slug:slug>', productviews.GetByCategoryId, name= 'category'),
    path('product/<int:product_id>/<slug:slug>', productviews.GetById, name= 'productdetail'),
    path('logout/', views.logout_view, name= 'logout'),
    path('signup/', views.signup_view, name= 'signup_view'),
    path('search/', productviews.product_search, name= 'product_search'),
    path('search_auto/', productviews.search_auto, name='search_auto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
