from rest_framework import viewsets, permissions

from products.models import Product
from products.serializers import ProductSerializer


class ProductListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.get_active_products()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})

        return context
