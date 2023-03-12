from django.urls import path

from .views import (
    UserCreateView,
    UserDeleteView,
    UsersListView,
    UserUpdateView,
)

urlpatterns = [
    path("", UsersListView.as_view(), name="users_lists"),
    path("create/", UserCreateView.as_view(), name="register"),
    path("<int:pk>/update/", UserUpdateView.as_view(), name="user_chg"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="user_del"),
]
