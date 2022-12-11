from adminsortable2.admin import SortableAdminMixin
from django.conf import settings
from django.contrib import admin
from django.utils.html import mark_safe

from .models import Work


@admin.register(Work)
class WorkAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("thumbnail", "name")
    fields = ("name", "image", "thumbnail")
    readonly_fields = ("thumbnail",)

    @admin.display()
    def thumbnail(self, obj) -> str:
        tag = f'<img src="{settings.MEDIA_URL}{obj.image}" height="100" />'
        return mark_safe(tag)
