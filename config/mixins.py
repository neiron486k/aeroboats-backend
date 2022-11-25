from django.db import models
from django.utils.translation import gettext_lazy as _


class NameModelMixin(models.Model):
    """Name field of model"""

    name = models.CharField(_("name"), max_length=100)

    class Meta:
        abstract = True

    def __str__(self) -> models.CharField:
        return self.name
