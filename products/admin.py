from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

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
