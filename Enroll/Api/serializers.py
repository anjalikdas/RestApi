from rest_framework import serializers
from Api.models import Customer, Product


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['status']
