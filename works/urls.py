from django.urls import path

from .views import WorkListApi

urlpatterns = [path("works/", WorkListApi.as_view(), name="work-list")]
