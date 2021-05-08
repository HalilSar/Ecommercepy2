from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin
from content.models import CImages, Menu, Content
class ContentImageInline(admin.TabularInline):
    model = CImages
    extra = 3 # ÜJ alan oluştur.

   
# Register your models here.
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title','type','image_tag','create_at','status')
    list_filter=['status','type']
    inlines = [ContentImageInline]
    prepopulated_fields = {'slug': ('title',)}
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
    

class MenuAdmin(DraggableMPTTAdmin):
    mptt_indent_field="title"
    list_display= ('status','indented_title','tree_actions')
    list_filter = ['status']

# Register your models here.
admin.site.register(Menu,MenuAdmin)
admin.site.register(Content,ContentAdmin)
# admin.site.register(CImages,MenuAdmin)