from django.db import models

from product.mixins import NameModelMixin, DetailsModelMixin
from product.models import Part


class Product(NameModelMixin, DetailsModelMixin, models.Model):
    parts = models.ManyToManyField(Part)

    class Meta:
        db_table = "product"


class Media(models.Model):
    """Media table for store product photos and video"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    path = models.FileField(upload_to="product")
