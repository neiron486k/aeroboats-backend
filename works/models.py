from django.db import models
from django.utils.translation import gettext_lazy as _

from .services import upload_image_path


class Work(models.Model):
    """Table store an images of completed works"""
    image = models.ImageField(_('image'), upload_to=upload_image_path)

    class Meta:
        db_table = "work"
        verbose_name = _("work")
        verbose_name_plural = _("works")

    def __str__(self) -> str:
        return str(self.id)
