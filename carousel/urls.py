from rest_framework import routers
from .views import CarouselViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r"carousels", CarouselViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
