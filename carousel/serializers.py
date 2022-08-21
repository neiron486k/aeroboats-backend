from rest_framework import serializers

from .models import Carousel


class CarouselSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carousel
        fields = "__all__"
