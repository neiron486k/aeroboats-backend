import math

from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        count = self.page.paginator.count

        return Response(
            {
                "links": {"next": self.get_next_link(), "previous": self.get_previous_link()},
                "total": count,
                "pages": math.ceil(count / self.get_page_size(self.request)),
                "page": self.page.number,
                "results": data,
            }
        )
