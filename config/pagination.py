from rest_framework import pagination
from rest_framework.response import Response
import math


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        count = self.page.paginator.count

        return Response(
            {
                "links": {"next": self.get_next_link(), "previous": self.get_previous_link()},
                "total": count,
                "pages": math.ceil(count / self.page_size),
                "page": self.page.number,
                "results": data,
            }
        )
