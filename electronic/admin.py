from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.html import format_html
from .models import Category, Manufacturer, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    def add_product_button(self, obj):
        return format_html('<a href="/admin/electronic/product/add_product/{}/">Добавить</a>', obj.id)

    add_product_button.short_description = 'Добавить 10 единиц товара'

    list_display = ('code','name','add_product_button', 'quantity')




admin.site.unregister([User, Group])