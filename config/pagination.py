import math
from collections import OrderedDict

from django.db.models import QuerySet
from rest_framework import pagination, views
from rest_framework.request import Request
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data: OrderedDict):
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


def get_paginated_response(*, serializer_class, queryset: QuerySet, request: Request, view: views.APIView):
    """Get the list of paginated data"""

    paginator = CustomPagination()
    page = paginator.paginate_queryset(queryset, request, view)

    if page is not None:
        serializer = serializer_class(page, many=True)

        return paginator.get_paginated_response(serializer.data)

    serializer = serializer_class(queryset, many=True)

    return Response(data=serializer.data)
