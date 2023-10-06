from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display=['title','description','active']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['title','description','sku']

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display=['id','product','file_path']

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display=['id','variant_title','variant','product']

@admin.register(ProductVariantPrice)
class ProductVariantPriceAdmin(admin.ModelAdmin):
    list_display=['id','product_variant_one','product_variant_two','product_variant_three','price' ,'stock' ,'product']