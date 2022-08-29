from rest_framework import routers

from products.views import ProductListViewSet

router = routers.DefaultRouter()
router.register(r"products", ProductListViewSet)

urlpatterns = router.urls
