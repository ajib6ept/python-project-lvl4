from django.urls import path

from .views import (
    TaskListView,
    TaskCreateView,
    TaskChangeView,
    TaskDeleteView,
    TaskDetailView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path(
        "<int:pk>/update/",
        TaskChangeView.as_view(),
        name="task_chd",
    ),
    path(
        "<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task_del",
    ),
    path("<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
]
