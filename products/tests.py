from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Product, Media


class TestProductListViewSet(APITestCase):
    def test_list(self):
        new_product = Product.objects.create(name="test product", description="test", price=100.50)
        Media.objects.create(path="path_to_file", product=new_product)

        response = self.client.get("/api/v1/products/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("results" in response.data.keys())

        product = response.data["results"][0]

        self.assertIn("id", product.keys())
        self.assertIn("name", product.keys())
        self.assertIn("description", product.keys())
        self.assertIn("price", product.keys())
        self.assertIn("media", product.keys())

        media_item = product["media"][0]

        self.assertIn("id", media_item.keys())
        self.assertIn("path", media_item.keys())
