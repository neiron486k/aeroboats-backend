from rest_framework import serializers

from .models import Slide


class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = "__all__"
