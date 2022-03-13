"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (
    HomePageView,
    UsersListView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
    UserLoginView,
    UserLogoutView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", UsersListView.as_view(), name="users_lists"),
    path("users/create/", UserCreateView.as_view(), name="user_create"),
    path("users/<int:pk>/update/", UserUpdateView.as_view(), name="user_chg"),
    path("users/<int:pk>/delete/", UserDeleteView.as_view(), name="user_del"),
    path("login/", UserLoginView.as_view(), name="user_login"),
    path("logout/", UserLogoutView.as_view(), name="user_logout"),
    path("", HomePageView.as_view(), name="home"),
]
