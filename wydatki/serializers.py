from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'is_staff']


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class ReceiptSerializer(serializers.ModelSerializer):
    #  products = serializers.PrimaryKeyRelatedField(read_only=True)
    # products = ProductSerializer(many=True, read_only=True)
    products = ProductSerializer(read_only=True,many=True)

    class Meta:
        model = Receipt
        fields = ['id', 'purchase_date', 'shop', 'products']
        depth = 1
