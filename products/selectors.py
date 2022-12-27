from django.http import Http404

from .models import Product
from django.db.models import QuerySet


def product_list() -> QuerySet[Product]:
    return Product.objects.all()


def product_get(product_id: int) -> Product:
    try:
        return Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404
