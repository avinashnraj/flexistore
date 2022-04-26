from rest_framework import serializers
from .models import Product
from .models import Uom

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'uom_id', 'price_per_unit']

class UomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uom
        fields = ['id', 'name']
