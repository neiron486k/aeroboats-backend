from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Product, Images


class TestProductListViewSet(APITestCase):
    def test_list(self):
        product = Product.objects.create(name="test product", description="test", price=100.50)
        image = Images.objects.create(path="", product=product)

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
        self.assertIn("description", product_keys)
        self.assertIn("price", product_keys)
        self.assertIn("images", product_keys)

        image = product["images"][0]
        image_keys = image.keys()

        self.assertIn("id", image_keys)
        self.assertIn("path", image_keys)
