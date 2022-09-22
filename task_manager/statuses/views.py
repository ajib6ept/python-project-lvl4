from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import DeleteView, FormView, UpdateView
from django.views.generic.list import ListView
from task_manager.mixins import TaskManagerLoginRequiredMixin

from .forms import StatusCreateForm
from .models import Status


class StatusListView(TaskManagerLoginRequiredMixin, ListView):
    template_name = "statuses/list.html"
    model = Status


class StatusCreateView(
    TaskManagerLoginRequiredMixin, SuccessMessageMixin, FormView
):
    template_name = "statuses/create.html"
    form_class = StatusCreateForm
    success_url = reverse_lazy("status_list")
    success_message = _("Статус успешно создан")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class StatusChangeView(
    TaskManagerLoginRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = Status
    template_name = "statuses/change.html"
    form_class = StatusCreateForm
    success_url = reverse_lazy("status_list")
    success_message = _("Статус успешно изменён")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class StatusDeleteView(
    TaskManagerLoginRequiredMixin, SuccessMessageMixin, DeleteView
):
    model = Status
    success_url = reverse_lazy("status_list")
    template_name = "statuses/delete.html"
    success_message = _("Статус успешно удалён")

    def form_valid(self, form, *args, **kwargs):
        object = self.get_object()
        if object.child_count > 0:
            error_msg = _("Вы не можете удалить статус, связаннный с задачей")
            messages.error(self.request, error_msg)
            return HttpResponseRedirect(self.success_url)
        return super().form_valid(form)
