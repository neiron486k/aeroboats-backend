from django.contrib import admin

from .models import Slide


@admin.register(Slide)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
