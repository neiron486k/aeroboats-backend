from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from products.managers import ProductManager
from products.mixins import NameModelMixin
from products.validators import file_size


class Product(NameModelMixin, models.Model):
    description = models.TextField(_("description"))
    price = models.FloatField(_("price"))
    is_active = models.BooleanField(_("active"), default=True)
    position = models.PositiveIntegerField(_("position"), default=0)

    class Meta:
        db_table = "product"
        verbose_name = _("product")
        verbose_name_plural = _("products")
        ordering = ["position"]

    objects = ProductManager()


class Media(models.Model):
    """Media model for store product photos and video"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="media")
    path = models.FileField(
        _("path"),
        upload_to="product",
        validators=[
            FileExtensionValidator(allowed_extensions=["png", "webp", "mp4", "mpv"]),
            file_size,
        ],
    )
