from django.urls import path
from .views import OrderCreateApi

urlpatterns = [path("orders/", OrderCreateApi.as_view(), name="order_create")]
