from re import search
from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["id"]


class IdProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(min_value=1)
