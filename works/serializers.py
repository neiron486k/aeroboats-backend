from rest_framework import serializers


class WorkSerializer(serializers.Serializer):  # noqa
    id = serializers.IntegerField()
    name = serializers.CharField()
    image = serializers.ImageField()
