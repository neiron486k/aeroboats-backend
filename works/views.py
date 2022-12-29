from rest_framework import permissions, generics

from .selectors import work_list
from .serializers import WorkSerializer


class WorkListApi(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = work_list()
    serializer_class = WorkSerializer
    pagination_class = None
