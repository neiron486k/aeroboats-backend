from rest_framework import status
from rest_framework.test import APITestCase


class TestProductListViewSet(APITestCase):
    def test_list(self):
        response = self.client.get("/api/v1/products/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
