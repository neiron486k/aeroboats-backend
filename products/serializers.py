from rest_framework import serializers

from products.models import Product, Images, ProductsSpecifications


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        exclude = ["product"]


class SpecificationSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField("_get_name")
    image = serializers.SerializerMethodField("_get_image")

    @staticmethod
    def _get_name(obj: ProductsSpecifications) -> str:
        return obj.specification.name

    def _get_image(self, obj: ProductsSpecifications) -> str:
        request = self.context.get("request")
        url = obj.specification.image.url

        if request:
            url = request.build_absolute_uri(url)

        return url

    class Meta:
        model = ProductsSpecifications
        fields = ["name", "image", "value"]


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    specifications = serializers.SerializerMethodField("_get_specifications")

    def _get_specifications(self, obj: Product) -> dict:
        product_spec = obj.productsspecifications_set.all()
        request = self.context.get("request")

        return SpecificationSerializer(product_spec, many=True, context={"request": request}).data

    class Meta:
        model = Product
        exclude = ["position", "is_active"]
