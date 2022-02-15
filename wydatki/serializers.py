from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'is_staff']


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'receipt_id']


class ReceiptSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True,write_only=True)
    class Meta:
        model = Receipt
        fields = ['id', 'purchase_date', 'shop', 'products']

    def create(self, validated_data):
        products = validated_data.pop('products')
        new_receipt = Receipt.objects.create(**validated_data)
        for i in products:
            Product.objects.create(**i,receipt=new_receipt)
        return new_receipt




