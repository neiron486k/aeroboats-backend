from rest_framework import serializers


def create_serializer_class(name: str, fields: dict) -> type:
    """Create a serializer"""

    return type(name, (serializers.Serializer,), fields)


def inline_serializer(*, fields, data=None, **kwargs) -> type:
    serializer_class = create_serializer_class(name="", fields=fields)

    if data is not None:
        return serializer_class(data=data, **kwargs)

    return serializer_class(**kwargs)
