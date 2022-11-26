from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from products.models import Product, Images, ProductsSpecifications


class ImageInline(admin.TabularInline):
    model = Images


class SpecificationInline(admin.TabularInline):
    model = ProductsSpecifications


@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    def get_queryset(self, request):
        return Product.objects.all()

    list_display = ("name", "price", "is_active")
    inlines = [ImageInline, SpecificationInline]
