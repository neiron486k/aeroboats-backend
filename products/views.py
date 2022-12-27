from rest_framework import permissions, views
from rest_framework.request import Request
from rest_framework.response import Response

from config.pagination import get_paginated_response
from .selectors import product_list, product_get
from .serializers import ProductListSerialiser, ProductDetailSerialiser


class ProductListApi(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: Request) -> Response:
        return get_paginated_response(
            serializer_class=ProductListSerialiser,
            queryset=product_list(),
            request=request,
            view=self
        )


class ProductDetailApi(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @staticmethod
    def get(request: Request, product_id: int) -> Response:
        product = product_get(product_id)
        serializer = ProductDetailSerialiser(product)

        return Response(serializer.data)
