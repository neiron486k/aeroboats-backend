from rest_framework import serializers

from config.serializers import inline_serializer
from products.models import Product, ProductsSpecifications


class SpecificationSerializer(serializers.Serializer):  # noqa
    name = serializers.SerializerMethodField("_get_name")
    image = serializers.SerializerMethodField("_get_image")
    value = serializers.CharField()

    @staticmethod
    def _get_name(obj: ProductsSpecifications) -> str:
        return obj.specification.name

    @staticmethod
    def _get_image(obj: ProductsSpecifications) -> str:
        return obj.specification.image.url


class ProductListSerialiser(serializers.Serializer):  # noqa
    id = serializers.IntegerField()
    name = serializers.CharField()
    short_description = serializers.CharField()
    image = serializers.ImageField()
    price = serializers.IntegerField()


class ProductDetailSerialiser(ProductListSerialiser):  # noqa
    description = serializers.CharField()
    images = inline_serializer(
        many=True,
        fields={
            "path": serializers.ImageField(),
        },
    )
    specifications = serializers.SerializerMethodField("_get_specifications")

    @staticmethod
    def _get_specifications(obj: Product) -> dict:
        product_specifications = obj.productsspecifications_set.all()
        return SpecificationSerializer(product_specifications, many=True).data
