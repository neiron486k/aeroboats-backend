from django.urls import path

from .views import ProductListApi, ProductDetailApi

urlpatterns = [
    path("products/", ProductListApi.as_view(), name='product-list'),
    path("products/<int:product_id>/", ProductDetailApi.as_view(), name='product-detail'),
]
