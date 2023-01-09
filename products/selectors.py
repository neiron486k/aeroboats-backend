from django.db.models import QuerySet

from .models import Product, ProductsSpecifications


def product_list() -> QuerySet[Product]:
    return Product.objects.filter(is_active=True)


def product_specifications_set(product: Product) -> QuerySet[ProductsSpecifications]:
    return product.productsspecifications_set.prefetch_related("specification")
