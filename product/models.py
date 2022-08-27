from django.db import models

from .mixins import NameModelMixin


class Product(NameModelMixin, models.Model):
    description = models.TextField()

    class Meta:
        db_table = "product"


class Category(NameModelMixin, models.Model):
    """Product categories"""

    products = models.ManyToManyField(Product)


class Media(models.Model):
    """Media table for store product photos and video"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    path = models.FileField(upload_to="product")
