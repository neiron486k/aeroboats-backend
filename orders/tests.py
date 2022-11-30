from rest_framework import status, exceptions
from rest_framework.test import APITestCase

from products.models import Product


class TestCreateOrderView(APITestCase):
    url = "/api/v1/orders/"

    def test_create(self):
        product = Product.objects.create(name="test product", description="test", price=100.50)
        data = {
            "product": product.id,
            "full_name": "John Doa",
            "phone": "+79213594494",
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_negative_create(self):
        response = self.client.post(self.url)
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(data["full_name"][0], exceptions.ErrorDetail)
        self.assertIsInstance(data["phone"][0], exceptions.ErrorDetail)
        self.assertIsInstance(data["product"][0], exceptions.ErrorDetail)
