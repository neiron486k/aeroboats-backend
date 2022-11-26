from rest_framework import viewsets, permissions

from .models import Work
from .serializers import WorkSerializer


class WorkListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = None
