from django.contrib import admin
from .models import Category, Product


# Модель категорий
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order_of_display']
    list_filter = ['order_of_display']
    list_editable = ['order_of_display']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_filter = ['name']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}
