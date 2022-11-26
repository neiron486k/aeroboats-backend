from rest_framework import serializers

from products.models import Product, Images, ProductsSpecifications


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        exclude = ["product"]


class SpecificationSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('_get_name')
    image = serializers.SerializerMethodField('_get_image')

    @staticmethod
    def _get_name(obj: ProductsSpecifications) -> str:
        return obj.specification.name

    @staticmethod
    def _get_image(obj: ProductsSpecifications) -> str:
        return obj.specification.image.url

    class Meta:
        model = ProductsSpecifications
        fields = ['name', 'image', 'value']


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    specifications = serializers.SerializerMethodField('_get_specifications')

    @staticmethod
    def _get_specifications(obj: Product) -> dict:
        product_spec = obj.productsspecifications_set.all()
        return SpecificationSerializer(product_spec, many=True).data

    class Meta:
        model = Product
        exclude = ["position", "is_active"]
