from django.db import models

from .mixins import NameModelMixin


class Category(NameModelMixin, models.Model):
    """Product categories"""

    class Meta:
        verbose_name_plural = "Categories"


class Product(NameModelMixin, models.Model):
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    price = models.FloatField(default=0)

    class Meta:
        db_table = "product"


class Media(models.Model):
    """Media table for store product photos and video"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    path = models.FileField(upload_to="product")
