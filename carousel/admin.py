from django.contrib import admin

from .models import Slide


class CarouselAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "thumbnail_min",
    )
    readonly_fields = ("thumbnail_preview",)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = "Thumbnail Preview"
    thumbnail_preview.allow_tags = True


admin.site.register(Slide, CarouselAdmin)
