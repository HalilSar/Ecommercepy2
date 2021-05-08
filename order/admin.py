from django.contrib import admin

# Register your models here.

from .models import ShopCart, Order, OrderProduct

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product','user','username','price','quantity','amount' ]
    list_filter = ['user']

class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product','price','quantity','amount')
    can_delete = False
    extra = 0
# Bunlar silinmesin değiştirilmesin Çünkü bunlar sadece readonly
#  OrderProduct sadece raporlama için kullanılır.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','phone','city','total','status']
    list_filter = ['status']
    readonly_fields = ('user','address','city','country','phone','first_name','ip', 'last_name','phone','city','total')
    inlines = [OrderProductline]

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product','price','quantity','amount']
    list_filter = ['user']

admin.site.register(ShopCart,ShopCartAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)
# admin.site.register(ShopCart,ShopCartAdmin)