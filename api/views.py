from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from electronic.models import Category, Manufacturer, Product
from .serializers import ProductSerializer
from .filters import TypeManufacturerFilter


class ProductViewSet(viewsets.ModelViewSet):
    """
    CRUD товара
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'code'
    filter_class = TypeManufacturerFilter

    def list(self, request, *args, **kwargs):
        params = request.GET

        if 'type' in params:
            if not Category.objects.filter(name=params['type']).exists():
                return Response(
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                    data={'error': 'Данный тип товара отсутствует в базе данных'}
                )
        elif 'manufacturer' in params:
            if not Manufacturer.objects.filter(name=params['manufacturer']).exists():
                return Response(
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                    data={'error': 'Данный производитель отсутствует в базе данных'}
                )
        else:
            return Response(status=404)

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProductListView(ListAPIView):
    """
    Список товара
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SummaryProductView(APIView):
    """
    Сумма товара
    """

    def get(self, request):
        product = Product.objects.all()
        params = request.GET

        if 'type' in params:
            if not Category.objects.filter(name=params['type']).exists():
                return Response(
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                    data={'error': 'Данный тип товара отсутствует в базе данных'}
                )
            else:
                product = product.filter(category__name__icontains=params['type'])

        if 'manufacturer' in params:
            if not Manufacturer.objects.filter(name=params['manufacturer']).exists():
                return Response(
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                    data={'error': 'Данный производитель отсутствует в базе данных'}
                )
            else:
                product = product.filter(manufacturer__name__icontains=params['manufacturer'])

        total_cost = sum([item.get_cost() for item in product])
        data = {'total_cost': total_cost}
        return Response(data)
