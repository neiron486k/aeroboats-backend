from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.conf import settings
from django.utils.html import mark_safe

from products.models import Product, ProductImage, ProductVideo, ProductsSpecifications


class ImageInline(admin.TabularInline):
    model = ProductImage


class VideoInline(admin.TabularInline):
    model = ProductVideo


class SpecificationInline(admin.TabularInline):
    model = ProductsSpecifications


@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("name", "price", "is_active")
    inlines = [ImageInline, VideoInline, SpecificationInline]


@admin.register(ProductImage)
class ProductImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_filter = ("product",)
    list_display = ("product", "thumbnail")

    @admin.display()
    def thumbnail(self, obj: ProductImage) -> str:
        tag = f'<img src="{settings.MEDIA_URL}{obj.image}" height="100" />'
        return mark_safe(tag)


@admin.register(ProductVideo)
class ProductImageAdmin(admin.ModelAdmin):
    list_filter = ("product",)
    list_display = ("product", "video")
