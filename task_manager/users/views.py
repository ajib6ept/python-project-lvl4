from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, FormView, UpdateView
from django.views.generic.list import ListView

from .forms import TaskManagerChangeUserForm, TaskManagerUserCreationForm
from .mixins import TaskUserAuthorizationMixin
from .models import TaskUser


class UsersListView(ListView):
    template_name = "users/list.html"
    model = TaskUser


class UserCreateView(SuccessMessageMixin, FormView):
    template_name = "users/register.html"
    form_class = TaskManagerUserCreationForm
    success_url = reverse_lazy("user_login")
    success_message = "Пользователь успешно зарегистрирован"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserUpdateView(
    SuccessMessageMixin, TaskUserAuthorizationMixin, UpdateView
):
    model = TaskUser
    template_name = "users/change.html"
    form_class = TaskManagerChangeUserForm
    success_url = reverse_lazy("users_lists")
    success_message = "Пользователь успешно изменён"


class UserDeleteView(
    SuccessMessageMixin, TaskUserAuthorizationMixin, DeleteView
):
    model = TaskUser
    success_url = reverse_lazy("users_lists")
    template_name = "users/delete.html"
    success_message = "Пользователь успешно удалён"
