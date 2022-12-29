from rest_framework import generics, permissions

from .serialiazers import OrderCreateSerializer
from .services import order_create


class OrderCreateApi(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderCreateSerializer

    def perform_create(self, serializer: OrderCreateSerializer) -> None:
        order_create(serializer.validated_data)
