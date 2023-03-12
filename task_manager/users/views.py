from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import DeleteView, FormView, UpdateView
from django.views.generic.list import ListView

from task_manager.users.forms import (
    TaskManagerChangeUserForm,
    TaskManagerUserCreationForm,
)
from task_manager.users.mixins import TaskUserAuthorizationMixin
from task_manager.users.models import TaskUser


class UsersListView(ListView):
    template_name = "users/list.html"
    model = TaskUser


class UserCreateView(SuccessMessageMixin, FormView):
    template_name = "users/register.html"
    form_class = TaskManagerUserCreationForm
    success_url = reverse_lazy("user_login")
    success_message = _("Пользователь успешно зарегистрирован")

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
    success_message = _("Пользователь успешно изменён")


class UserDeleteView(
    SuccessMessageMixin, TaskUserAuthorizationMixin, DeleteView
):
    model = TaskUser
    success_url = reverse_lazy("users_lists")
    template_name = "users/delete.html"
    success_message = _("Пользователь успешно удалён")

    def form_valid(self, form, *args, **kwargs):
        object = self.get_object()
        if object.child_count > 0:
            error_msg = _(
                "Вы не можете удалить пользователя, связаннного с задачей"
            )
            messages.error(self.request, error_msg)
            return HttpResponseRedirect(self.success_url)
        return super().form_valid(form)
