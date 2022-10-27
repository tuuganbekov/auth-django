from django.db import models
from products.models import Product


# Create your models here.
class Purchase(models.Model):
    full_name = models.CharField(max_length=255)
    total_sum = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.full_name} - {self.total_sum}"


class PurchaseProduct(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField(default=0)
    sum = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.purchase} - {self.product}"
