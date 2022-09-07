from django.conf import settings
from django.db import models

from products.models import Product


class Basket(models.Model):
    """Basket for user and products"""

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    products = models.ManyToManyField(Product, through="BasketProducts")

    class Meta:
        db_table = "basket"


class BasketProducts(models.Model):
    """Products of basket"""

    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    class Meta:
        db_table = "basket_products"
