from rest_framework import serializers

from products.models import Product, Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        exclude = ["product"]


class ProductSerializer(serializers.ModelSerializer):
    media = MediaSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
