from django.urls import path
from .views import (
    StatusListView,
    StatusCreateView,
    StatusChangeView,
    StatusDeleteView,
)

urlpatterns = [
    path("", StatusListView.as_view(), name="status_list"),
    path("create/", StatusCreateView.as_view(), name="status_create"),
    path(
        "<int:pk>/update/",
        StatusChangeView.as_view(),
        name="status_chd",
    ),
    path(
        "<int:pk>/delete/",
        StatusDeleteView.as_view(),
        name="status_del",
    ),
]
