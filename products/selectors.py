from django.db.models import QuerySet

from .models import Product


def product_list() -> QuerySet[Product]:
    return Product.objects.all()
