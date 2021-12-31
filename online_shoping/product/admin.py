from django.contrib import admin
from .models import Category,Product

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name','description']
    list_filter=['name']

admin.site.register(Category,CategoryAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','description','category']
    list_filter=['price','category']

admin.site.register(Product,ProductAdmin)