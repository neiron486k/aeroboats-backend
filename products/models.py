from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _

from config.mixins import NameModelMixin
from config.validators import FileSizeValidator
from django.core.validators import FileExtensionValidator
from products.services import upload_media_path
from specifications.models import Specification
from config.mixins import PositionMixin


class Product( PositionMixin, NameModelMixin, models.Model):
    """Products of site"""

    short_description = models.TextField(_("short_description"), default="")
    description = RichTextField(_("description"))
    price = models.IntegerField(_("price"))
    is_active = models.BooleanField(_("active"), default=True)
    image = models.ImageField(
        _("image"),
        upload_to=upload_media_path,
        validators=[FileSizeValidator(2)],
        default="",
    )
    specifications = models.ManyToManyField(Specification, through="ProductsSpecifications")

    class Meta:
        db_table = "product"
        verbose_name = _("product")
        verbose_name_plural = _("products")
        ordering = ["position"]


class ProductImage(PositionMixin, models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(_("image"), upload_to=upload_media_path, validators=[FileSizeValidator(2)])

    class Meta:
        db_table = "product_images"
        ordering = ["position"]


class ProductVideo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="videos")
    video = models.FileField(
        _("video"),
        upload_to=upload_media_path,
        validators=[FileSizeValidator(10), FileExtensionValidator(allowed_extensions=("avi", "mp4"))],
    )

    class Meta:
        db_table = "product_videos"


class ProductsSpecifications(PositionMixin, models.Model):
    """Pivot table for products and specifications"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(Specification, on_delete=models.CASCADE)
    value = models.CharField(_("value"), max_length=255)

    class Meta:
        db_table = "products_specifications"
        unique_together = (
            "product",
            "specification",
        )
        verbose_name = _("product specifications")
        verbose_name_plural = _("product specifications")
        ordering = ["position"]
