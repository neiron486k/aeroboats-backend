import shutil

from rest_framework import status
from rest_framework.test import APITestCase, override_settings

from .factories import ProductWithSpecificationFactory

MEDIA_ROOT = "/tmp/upload"


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class TestProductListViewSet(APITestCase):
    def setUp(self) -> None:
        self.product = ProductWithSpecificationFactory.create(images=1, videos=1)

    def test_list(self) -> None:
        response = self.client.get("/api/v1/products/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        paginated_keys = response.data.keys()

        self.assertIn("links", paginated_keys)
        self.assertIn("total", paginated_keys)
        self.assertIn("pages", paginated_keys)
        self.assertIn("page", paginated_keys)
        self.assertIn("results", paginated_keys)

        product_data = response.data["results"][0]
        product_keys = product_data.keys()

        self.assertIn("id", product_keys)
        self.assertIn("name", product_keys)
        self.assertIn("short_description", product_keys)
        self.assertIn("price", product_keys)
        self.assertIn("image", product_keys)

    def test_get(self) -> None:
        response = self.client.get(f"/api/v1/products/{self.product.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data
        image = data["images"][0]
        video = data["videos"][0]
        specification = data["specifications"][0]

        self.assertIn("id", data)
        self.assertIn("name", data)
        self.assertIn("short_description", data)
        self.assertIn("description", data)
        self.assertIn("price", data)
        self.assertIn("id", image)
        self.assertIn("image", image)
        self.assertIn("id", video)
        self.assertIn("video", video)
        self.assertIn("name", specification)
        self.assertIn("image", specification)
        self.assertIn("value", specification)

    def test_not_found(self) -> None:
        response = self.client.get(f"/api/v1/products/2/")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self) -> None:
        shutil.rmtree(MEDIA_ROOT)
