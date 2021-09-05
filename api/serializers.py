from rest_framework import serializers
from electronic.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор товара
    """
    gross_cost = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_gross_cost(self, obj):
        return obj.get_cost()
