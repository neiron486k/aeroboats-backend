from django.urls import path

from .views import CarouselViewSet

urlpatterns = [path("carousel/items", CarouselViewSet.as_view())]
