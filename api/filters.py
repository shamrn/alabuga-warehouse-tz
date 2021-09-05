from django_filters import rest_framework as filters
from electronic.models import Product


class TypeManufacturerFilter(filters.FilterSet):
    type = filters.CharFilter(field_name='category__name', lookup_expr='iexact')
    manufacturer = filters.CharFilter(field_name='manufacturer__name', lookup_expr='iexact')

    class Meta:
        model = Product
        fields = ('type', 'manufacturer')
