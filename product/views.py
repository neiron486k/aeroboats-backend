from rest_framework import generics, permissions

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
