from django.db.models import QuerySet

from .models import Work


def work_list() -> QuerySet[Work]:
    return Work.objects.all()
