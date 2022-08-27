from django.db import models


class NameModelMixin(models.Model):
    """Name field of table"""

    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self) -> models.CharField:
        return self.name
