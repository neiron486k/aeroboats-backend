from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Product


class TestCreateOrderView(APITestCase):
    def test_create(self):
        product = Product.objects.create(name="test product", description="test", price=100.50)
        data = {
            "product": product.pk,
            "full_name": "John Doa",
            "phone": "+79213594494",
        }

        url = '/api/v1/orders/'
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_negative_create(self):
        ...
