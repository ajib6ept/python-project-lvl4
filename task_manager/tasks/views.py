from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, FormView, UpdateView
from django_filters.views import FilterView

from task_manager.tasks.filters import TaskFilter
from task_manager.tasks.forms import TaskCreateForm
from task_manager.tasks.models import Task
from task_manager.mixins import TaskManagerLoginRequiredMixin


class TaskListView(TaskManagerLoginRequiredMixin, FilterView):
    template_name = "tasks/list.html"
    model = Task
    filterset_class = TaskFilter


class TaskCreateView(
    TaskManagerLoginRequiredMixin, SuccessMessageMixin, FormView
):
    template_name = "tasks/create.html"
    form_class = TaskCreateForm
    success_url = reverse_lazy("task_list")
    success_message = _("Задача успешно создана")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class TaskChangeView(
    TaskManagerLoginRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = Task
    template_name = "tasks/change.html"
    form_class = TaskCreateForm
    success_url = reverse_lazy("task_list")
    success_message = _("Задача успешно изменена")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TaskDeleteView(
    TaskManagerLoginRequiredMixin, SuccessMessageMixin, DeleteView
):
    model = Task
    success_url = reverse_lazy("task_list")
    template_name = "tasks/delete.html"
    success_message = _("Задача успешно удалена")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            error_message = _("Задачу может удалить только её автор")
            messages.error(request, error_message)
            return redirect("task_list")
        return super(TaskDeleteView, self).dispatch(request, *args, **kwargs)


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/detail.html"
