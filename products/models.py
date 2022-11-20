from django.db import models
from django.utils.translation import gettext_lazy as _

from config.validators import file_size
from products.managers import ProductManager
from products.mixins import NameModelMixin
from products.services import upload_image_path
from ckeditor.fields import RichTextField


class Product(NameModelMixin, models.Model):
    """Products of site"""

    short_description = models.TextField(_("short_description"), default='')
    description = RichTextField(_("description"))
    price = models.DecimalField(_("price"), decimal_places=2, max_digits=9)
    is_active = models.BooleanField(_("active"), default=True)
    position = models.PositiveIntegerField(_("position"), default=0)
    image = models.ImageField(
        _("image"),
        upload_to=upload_image_path,
        validators=[file_size],
        default="",
    )

    objects = ProductManager()

    class Meta:
        db_table = "product"
        verbose_name = _("product")
        verbose_name_plural = _("products")
        ordering = ["position"]


class Images(models.Model):
    """Media for store product photos and video"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    path = models.ImageField(_("path"), upload_to=upload_image_path, validators=[file_size])

    class Meta:
        db_table = "product_images"
