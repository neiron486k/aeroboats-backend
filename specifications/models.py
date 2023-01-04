from django.db import models
from config.mixins import NameModelMixin
from config.validators import validate_file_size
from django.utils.translation import gettext_lazy as _
from .services import upload_image_path


class Specification(NameModelMixin, models.Model):
    image = models.ImageField(upload_to=upload_image_path, validators=[validate_file_size])

    class Meta:
        db_table = "specification"
        verbose_name = _("specification")
        verbose_name_plural = _("specifications")
