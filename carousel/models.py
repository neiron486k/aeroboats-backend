from django.db import models
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html


class Carousel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="carousel", default="")

    class Meta:
        ordering = ["-id"]

    @property
    def thumbnail_preview(self) -> str:
        return self.__get_image()

    @property
    def thumbnail_min(self):
        return self.__get_image("70x70")

    def __get_image(self, size: str = "300x300"):
        if self.thumbnail:
            _thumbnail = get_thumbnail(
                self.thumbnail, size, upscale=False, crop=False, quality=100
            )

            return format_html(
                '<img src="{}" width="{}" height="{}">'.format(
                    _thumbnail.url, _thumbnail.width, _thumbnail.height
                )
            )

        return ""

    def __str__(self) -> models.CharField:
        return self.title
