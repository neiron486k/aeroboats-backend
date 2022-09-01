from django.db import models
from django.core.validators import FileExtensionValidator

from config.validators import file_size
from .services import upload_slide_path


class Slide(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cover = models.FileField(
        upload_to=upload_slide_path,
        default="",
        validators=[
            FileExtensionValidator(allowed_extensions=["png", "webp", "mp4", "mpv"]),
            file_size,
        ],
    )

    class Meta:
        ordering = ["-id"]

    def __str__(self) -> models.CharField:
        return self.title
