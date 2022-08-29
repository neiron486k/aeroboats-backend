from django.contrib import admin

from products.models import Product, Media


class MediaInline(admin.TabularInline):
    model = Media


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_active")
    inlines = [MediaInline]
