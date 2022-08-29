from django.db import models

from products.mixins import NameModelMixin


class Product(NameModelMixin, models.Model):
    description = models.TextField()
    price = models.FloatField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "product"
        ordering = ["-id"]


class Media(models.Model):
    """Media table for store product photos and video"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="media")
    path = models.FileField(upload_to="product")
