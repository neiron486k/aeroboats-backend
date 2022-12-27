from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Product, Images, ProductsSpecifications
from specifications.models import Specification


class TestProductListViewSet(APITestCase):
    def test_list(self) -> None:
        product = Product.objects.create(name="test product", description="test", price=100.50)
        Images.objects.create(path="", product=product)

        response = self.client.get("/api/v1/products/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        paginated_keys = response.data.keys()

        self.assertIn("links", paginated_keys)
        self.assertIn("total", paginated_keys)
        self.assertIn("pages", paginated_keys)
        self.assertIn("page", paginated_keys)
        self.assertIn("results", paginated_keys)

        product = response.data["results"][0]
        product_keys = product.keys()

        self.assertIn("id", product_keys)
        self.assertIn("name", product_keys)
        self.assertIn("short_description", product_keys)
        self.assertIn("price", product_keys)

    def test_get(self) -> None:
        product = Product.objects.create(
            name="test product", short_description="some text", description="some large test", price=100.50
        )
        Images.objects.create(path="", product=product)
        image_file = SimpleUploadedFile(name="test_image.jpg", content="", content_type="image/jpeg")
        specification = Specification.objects.create(name="test_specification", image=image_file)
        ProductsSpecifications.objects.create(product=product, specification=specification, value=100)

        response = self.client.get(f"/api/v1/products/{product.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data
        image = data["images"][0]
        specification = data["specifications"][0]

        self.assertIn("id", data)
        self.assertIn("name", data)
        self.assertIn("short_description", data)
        self.assertIn("description", data)
        self.assertIn("price", data)
        self.assertIn("path", image)
        self.assertIn("name", specification)
        self.assertIn("image", specification)
        self.assertIn("value", specification)

    def test_not_found(self) -> None:
        response = self.client.get(f"/api/v1/products/2/")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
