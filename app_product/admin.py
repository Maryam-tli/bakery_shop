from django.contrib import admin
from app_product.models import *

# Register your models here.
class Pro_CategoryAdmin(admin.ModelAdmin):
    fields = ['name','slug']
    list_display = ['name',]

admin.site.register(Pro_Category, Pro_CategoryAdmin)

class ProductTypeAdmin(admin.ModelAdmin):
    fields = ['name',]
    list_display = ['name',]

admin.site.register(ProductType, ProductTypeAdmin)

class FlavorAdmin(admin.ModelAdmin):
    fields = ['name','product_type']
    list_display = ['name','product_type']

admin.site.register(Flavor, FlavorAdmin)

class ProductAdmin(admin.ModelAdmin):
    fields = ['name','slug','product_type','flavor','pro_category','description','price','discount_percent','image','available', 'status']
    list_display = ['name','price','discount_percent','available','get_final_price', 'status']
    search_fields = ['name', 'discount_percent','available','pro_category']
    
    def get_final_price(self, obj):
        return f"{obj.get_final_price():.2f}"
    get_final_price.short_description = 'Final Price'


admin.site.register(Product, ProductAdmin)

class ProductImageAdmin(admin.ModelAdmin):
    fields =['product', 'file']
    list_display = ['product',]
    search_fields = ['product',]

admin.site.register(ProductImage,ProductImageAdmin )