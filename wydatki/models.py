from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Receipt(models.Model):
    purchase_date = models.DateTimeField(auto_now=True, null=False)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    receipt = models.ForeignKey(Receipt, on_delete=models.SET_NULL, null=True, related_name='products')

    def __str__(self):
        return self.name
