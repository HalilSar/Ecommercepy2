from django.urls import path
from . import views

urlpatterns = [
    path('user-profile/',views.index, name="profile"),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.user_password, name='user_password'),
    path('orders/', views.user_orders, name='user_orders'),
    path('orderdetail/<int:id>', views.user_orderdetail, name='user_orderdetail'),
    path('comments/', views.user_comments, name='user_comment'),
    path('deletecomment/<int:id>', views.user_deletecomment, name='delete_comment'),
]