from django.contrib import admin

from .models import Product, Media


class MediaInline(admin.TabularInline):
    model = Media


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [MediaInline]
