from django.db.models.manager import Manager
from django.db.models.query import QuerySet


class ProductManager(Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().prefetch_related("media")

    def get_active_products(self) -> QuerySet:
        return self.get_queryset().filter(is_active=True)
