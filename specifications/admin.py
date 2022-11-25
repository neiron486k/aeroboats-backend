from django.contrib import admin
from .models import Specification
from PIL import Image


class SpecificationAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        image = Image.open(obj.image.path)

        if image.height >= 200 or image.width >= 200:
            new_img = (100, 100)
            image.thumbnail(new_img)
            image.save(obj.image.path)


admin.site.register(Specification, SpecificationAdmin)
