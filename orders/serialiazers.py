from rest_framework import serializers
from .models import Order
from drf_recaptcha.fields import ReCaptchaV3Field


class OrderSerializer(serializers.ModelSerializer):
    recaptcha = ReCaptchaV3Field(action="order", write_only=True)

    def validate(self, attrs) -> dict:
        attrs.pop("recaptcha")

        return attrs

    class Meta:
        model = Order
        fields = "__all__"
