from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from wydatki.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [AllowAny]

    @action(methods=['get'], detail=True)
    def receipts(self, request, pk=None):
        receipts = Receipt.objects.filter(shop_id=pk)
        serialized_receipts = ReceiptSerializer(receipts, many=True)
        return Response(serialized_receipts.data)


class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    permission_classes = [AllowAny]

    @action(methods=['get'], detail=True)
    #detail true = mozna sie odwolywac do pojedynczej encji (id),
    #bez tego metoda zwracala by wszystkie obiekty
    def products(self, request, pk=None):
        products = Product.objects.filter(receipt_id=pk)
        serialized_products = ProductSerializer(products, many=True)
        return Response(serialized_products.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]