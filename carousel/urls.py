from django.urls import path

from .views import CarouselViewSet

urlpatterns = [path("carousel/slides", CarouselViewSet.as_view())]
