from django.db.models.manager import Manager


class ProductManager(Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_active_products(self):
        return self.get_queryset().filter(is_active=True)
