from rest_framework import generics, permissions

from .serialiazers import OrderCreateSerializer
from .services import OrderService


class OrderCreateApi(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderCreateSerializer
    service = OrderService()

    def perform_create(self, serializer: OrderCreateSerializer) -> None:
        self.service.create(serializer.validated_data)
