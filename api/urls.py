from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, ProductListView, SummaryProductView


api_router = routers.DefaultRouter()
api_router.register(r'', ProductViewSet)

urlpatterns = [
    path('all/', ProductListView.as_view()),
    path('summary/', SummaryProductView.as_view()),
    path('', include(api_router.urls)),
]