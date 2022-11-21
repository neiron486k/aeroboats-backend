from rest_framework import routers

from .views import WorkListViewSet

router = routers.DefaultRouter()
router.register(r"works", WorkListViewSet)

urlpatterns = router.urls
