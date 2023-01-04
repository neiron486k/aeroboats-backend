from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _

from config.mixins import NameModelMixin
from config.validators import validate_file_size
from products.services import upload_media_path
from specifications.models import Specification
from config.fields import RestrictedFileField


class Product(NameModelMixin, models.Model):
    """Products of site"""

    short_description = models.TextField(_("short_description"), default="")
    description = RichTextField(_("description"))
    price = models.IntegerField(_("price"))
    is_active = models.BooleanField(_("active"), default=True)
    position = models.PositiveIntegerField(_("position"), default=0)
    image = models.ImageField(
        _("image"),
        upload_to=upload_media_path,
        validators=[validate_file_size],
        default="",
    )
    specifications = models.ManyToManyField(Specification, through="ProductsSpecifications")

    class Meta:
        db_table = "product"
        verbose_name = _("product")
        verbose_name_plural = _("products")
        ordering = ["position"]


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(_("image"), upload_to=upload_media_path, validators=[validate_file_size])
    position = models.PositiveIntegerField(_("position"), default=0)

    class Meta:
        db_table = "product_images"
        ordering = ["position"]


class ProductVideo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="videos")
    video = RestrictedFileField(_("video"), upload_to=upload_media_path, max_upload_size=200, extensions=[".mp4"])

    class Meta:
        db_table = "product_videos"


class ProductsSpecifications(models.Model):
    """Pivot table for products and specifications"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(Specification, on_delete=models.CASCADE)
    value = models.CharField(_("value"), max_length=255)
    position = models.PositiveIntegerField(_("position"), default=0)

    class Meta:
        db_table = "products_specifications"
        unique_together = (
            "product",
            "specification",
        )
        verbose_name = _("product specifications")
        verbose_name_plural = _("product specifications")
        ordering = ["position"]
