from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'size', 'color', 'in_stock')
    list_filter = ('category', 'size', 'in_stock')
    search_fields = ('name', 'description', 'color')
    list_editable = ('price', 'in_stock')
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description', 'category', 'price', 'image')
        }),
        ('Характеристики', {
            'fields': ('size', 'color', 'material')
        }),
        ('Наличие', {
            'fields': ('in_stock',)
        }),
    )