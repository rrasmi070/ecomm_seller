from django.contrib import admin
from api.models import Category,Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'Product_name', 'brand', 'Description', 'Price']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']


admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)