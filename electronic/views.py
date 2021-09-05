from django.shortcuts import render, redirect
from .models import Product


def add_product(request, pk):
    """
    Добавляем 10 ед. товара
    """
    product = Product.objects.get(pk=pk)
    product.quantity += 10
    product.save()
    return redirect('/admin/electronic/product')
