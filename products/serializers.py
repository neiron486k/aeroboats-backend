from rest_framework import serializers

from products.models import Product, Images


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        exclude = ["product"]


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        exclude = ["position", "is_active"]
