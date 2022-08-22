from rest_framework import viewsets, permissions, generics

from .models import Carousel
from .serializers import CarouselSerializer


class CarouselViewSet(generics.ListAPIView):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer
    permission_classes = [permissions.AllowAny]
