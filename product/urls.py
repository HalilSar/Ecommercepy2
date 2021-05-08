from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='product'),
    path('addcomment/<int:id>', views.addcomment, name='addcomment'),
    # path('search/', views.search, name='search'),
    # path('category/<int:category_id>/<slug:slug>', views.GetByCategoryId, name= 'category'),
]

    