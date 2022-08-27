from django.contrib import admin

from .models import Product, Media, Category


class MediaInline(admin.TabularInline):
    model = Media


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [MediaInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ["name"]
