from django.core.validators import FileExtensionValidator
from django.db import models

from config.validators import file_size, allowed_file_extension
from .services import upload_slide_path


class Slide(models.Model):
    """Slide of carousel"""

    title = models.CharField(max_length=100)
    description = models.TextField()
    cover = models.FileField(
        upload_to=upload_slide_path,
        default="",
        validators=[
            FileExtensionValidator(allowed_extensions=allowed_file_extension()),
            file_size,
        ],
    )

    class Meta:
        ordering = ["-id"]

    def __str__(self) -> models.CharField:
        return self.title
