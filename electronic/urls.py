from django.urls import path
from . import views

urlpatterns = [
    path('admin/electronic/product/add_product/<pk>/', views.add_product),
]