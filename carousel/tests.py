from rest_framework import status
from rest_framework.test import APITestCase

from carousel.models import Slide


class TestCarousel(APITestCase):
    def test_get_items(self):
        Slide.objects.create(
            title="test title", description="test description", thumbnail="image_url"
        )

        response = self.client.get("/api/v1/carousel/slides/")
        carousel_item = response.data[0]
        carousel_item_keys = carousel_item.keys()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("title" in carousel_item_keys)
        self.assertTrue("thumbnail" in carousel_item_keys)
        self.assertTrue("description" in carousel_item_keys)
