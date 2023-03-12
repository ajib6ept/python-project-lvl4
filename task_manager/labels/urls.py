from django.urls import path

from .views import (
    LabelChangeView,
    LabelCreateView,
    LabelDeleteView,
    LabelListView,
)

urlpatterns = [
    path("", LabelListView.as_view(), name="label_list"),
    path("create/", LabelCreateView.as_view(), name="label_create"),
    path(
        "<int:pk>/update/",
        LabelChangeView.as_view(),
        name="label_chd",
    ),
    path(
        "<int:pk>/delete/",
        LabelDeleteView.as_view(),
        name="label_del",
    ),
]
