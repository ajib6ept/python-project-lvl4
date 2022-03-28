from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.list import ListView


from .forms import (
    TaskManagerChangeUserForm,
    TaskManagerUserCreationForm,
)


class UsersListView(ListView):
    template_name = "users/list.html"
    model = User


class UserCreateView(SuccessMessageMixin, FormView):
    template_name = "users/register.html"
    form_class = TaskManagerUserCreationForm
    success_url = reverse_lazy("user_login")
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = User
    template_name = "users/change.html"
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
    template_name = "users/delete.html"

    def dispatch(self, *args, **kwargs):
        obj = self.get_object()
        if obj != self.request.user:
            return redirect("user_login")
        return super().dispatch(*args, **kwargs)