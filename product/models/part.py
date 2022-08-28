from django.db import models

from product.mixins import NameModelMixin, DetailsModelMixin


class Category(NameModelMixin, models.Model):
    """Part category"""

    class Meta:
        db_table = "part_category"
        verbose_name_plural = "Categories"


class Part(NameModelMixin, DetailsModelMixin, models.Model):
    """Parts of product"""

    image = models.ImageField(upload_to="part", default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "part"
