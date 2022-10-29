from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from products.models import Product, Images


class ImageInline(admin.TabularInline):
    model = Images


@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    def get_queryset(self, request):
        return Product.objects.all()

    list_display = ("name", "price", "is_active")
    inlines = [ImageInline]
