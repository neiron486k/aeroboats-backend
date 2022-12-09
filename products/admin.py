from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.utils.html import mark_safe

from products.models import Product, Images, ProductsSpecifications


class ImageInline(admin.TabularInline):
    extra = 1
    model = Images


class SpecificationInline(admin.TabularInline):
    extra = 1
    model = ProductsSpecifications


@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("image_list", "name", "price", "is_active")
    readonly_fields = ("image_list", "image_preview")
    fields = ("name", "short_description", "description", "price", "image", "image_preview", "is_active")
    inlines = [ImageInline, SpecificationInline]

    @admin.display(description="image_list")
    def image_list(self, obj):
        return mark_safe('<img src="/upload/%s" width="70" height="70" />' % obj.image)

    @admin.display(description="image_preview")
    def image_preview(self, obj):
        return mark_safe('<img src="/upload/%s" width="100" height="100" />' % obj.image)
