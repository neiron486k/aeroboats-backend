from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Product, Media


class TestProductListViewSet(APITestCase):
    def test_list(self):
        new_product = Product.objects.create(name="test product", description="test", price=100.50)
        Media.objects.create(path="path_to_file", product=new_product)

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
        self.assertIn("description", product_keys)
        self.assertIn("price", product_keys)
        self.assertIn("media", product_keys)

        media_item = product["media"][0]
        media_item_keys = media_item.keys()

        self.assertIn("id", media_item_keys)
        self.assertIn("path", media_item_keys)
