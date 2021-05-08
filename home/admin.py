from django.contrib import admin
from .models import Setting
from .models import ContactFormMessage
from .models import UserProfile
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','status']
    liist_filter = ['status']
class UserFormAdmin(admin.ModelAdmin):
    list_display = ['user_name','image_tag']
    liist_filter = ['status']


admin.site.register(Setting)
admin.site.register(ContactFormMessage,ContactFormAdmin)
admin.site.register(UserProfile,UserFormAdmin)
