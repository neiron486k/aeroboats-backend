from rest_framework import viewsets, permissions

from .models import Carousel
from .serializers import CarouselSerializer


class CarouselViewSet(viewsets.ModelViewSet):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer
    permission_classes = [permissions.AllowAny]
