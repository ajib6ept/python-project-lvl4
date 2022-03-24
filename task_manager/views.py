from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.list import ListView


from .forms import (
    TaskManagerAuthenticationForm,
    TaskManagerChangeUserForm,
    TaskManagerUserCreationForm,
    StatusCreateForm,
)

from .models import Status


class HomePageView(TemplateView):
    template_name = "home.html"


class UsersListView(ListView):
    template_name = "users_list.html"
    model = User


class UserCreateView(SuccessMessageMixin, FormView):
    template_name = "user_register.html"
    form_class = TaskManagerUserCreationForm
    success_url = reverse_lazy("user_login")
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = User
    template_name = "user_change.html"
    form_class = TaskManagerChangeUserForm
    success_url = reverse_lazy("users_lists")
    success_message = "Your profile was created successfully"

    def dispatch(self, *args, **kwargs):
        obj = self.get_object()
        if obj != self.request.user:
            return redirect("user_login")
        return super().dispatch(*args, **kwargs)


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy("users_lists")
    template_name = "user_delete.html"

    def dispatch(self, *args, **kwargs):
        obj = self.get_object()
        if obj != self.request.user:
            return redirect("user_login")
        return super().dispatch(*args, **kwargs)


class UserLoginView(SuccessMessageMixin, FormView):
    template_name = "user_login.html"
    success_url = reverse_lazy("home")
    form_class = TaskManagerAuthenticationForm
    success_message = "Successful login"

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("home")


class StatusListView(LoginRequiredMixin, ListView):
    template_name = "status_list.html"
    model = Status


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = "status_create.html"
    form_class = StatusCreateForm
    success_url = reverse_lazy("status_list")
    success_message = "Your status was created successfully"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class StatusChangeView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    template_name = "status_change.html"
    form_class = StatusCreateForm
    success_url = reverse_lazy("status_list")
    success_message = "Your status was changed successfully"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    success_url = reverse_lazy("status_list")
    template_name = "status_delete.html"
