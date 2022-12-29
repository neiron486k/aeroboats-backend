from rest_framework import status, exceptions
from rest_framework.test import APITestCase

from products.models import Product
from .models import Order
from .enums import Status


class TestCreateOrderView(APITestCase):
    url = "/api/v1/orders/"

    def test_create(self):
        with self.settings(DRF_RECAPTCHA_TESTING=True):
            product = Product.objects.create(name="test product", description="test", price=100)
            data = {
                "product": product.id,
                "full_name": "John Doa",
                "phone": "+79213594494",
                "recaptcha": "test",
                "price": 100,
            }

            response = self.client.post(self.url, data)

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            order = Order.objects.last()

            self.assertEqual(100, order.price)
            self.assertEqual(Status.NEW, order.status)

    def test_negative_create(self):
        response = self.client.post(self.url)
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(data["full_name"][0], exceptions.ErrorDetail)
        self.assertIsInstance(data["phone"][0], exceptions.ErrorDetail)
        self.assertIsInstance(data["product"][0], exceptions.ErrorDetail)
