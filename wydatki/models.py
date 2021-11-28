from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=200)

class Receipt(models.Model):
    purchase_date = models.DateTimeField(auto_now=True, null=False)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)

class Product(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)



