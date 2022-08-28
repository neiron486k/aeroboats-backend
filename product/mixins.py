from django.db import models


class NameModelMixin(models.Model):
    """Name field of model"""

    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self) -> models.CharField:
        return self.name


class DetailsModelMixin(models.Model):
    """Details for product model"""

    price = models.FloatField(default=0)
    description = models.TextField()

    class Meta:
        abstract = True
