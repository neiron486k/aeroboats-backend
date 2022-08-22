from rest_framework import viewsets, permissions, generics

from .models import Slide
from .serializers import CarouselSerializer


class CarouselViewSet(generics.ListAPIView):
    queryset = Slide.objects.all()
    serializer_class = CarouselSerializer
    permission_classes = [permissions.AllowAny]
