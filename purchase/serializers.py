from rest_framework import serializers
from products.serializers import ProductSerializer


class PurchaseSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    products = ProductSerializer(many=True)
