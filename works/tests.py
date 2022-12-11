from rest_framework import status
from rest_framework.test import APITestCase
from .models import Work


class WorkListViewSetTest(APITestCase):
    def test_list(self):
        Work.objects.create()
        response = self.client.get("/api/v1/works/")
        serialized_work = response.data[0]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("id", serialized_work.keys())
        self.assertIn("image", serialized_work.keys())
        self.assertIn("name", serialized_work.keys())
