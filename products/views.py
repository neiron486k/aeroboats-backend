from rest_framework import permissions, generics

from .selectors import product_list
from .serializers import ProductListSerialiser, ProductDetailSerialiser


class ProductListApi(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProductListSerialiser
    queryset = product_list()


class ProductDetailApi(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProductDetailSerialiser
    queryset = product_list()
