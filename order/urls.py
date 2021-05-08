from django.urls import include, path
from . import views

urlpatterns=[
    path('',views.index, name='index'),
   
    # path('shopcart/',views.shopcart, name="shopcart")
    # path('addtocart/<int:id>',views.addtocart,name="addtocart"),
    # path('deletetocart/<int:id>',views.deletetocart,name="deletetocart")
]