from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, FormView, UpdateView
from django.views.generic.list import ListView
from django_filters.views import FilterView

from .filters import TaskFilter
from .forms import TaskCreateForm
from .models import Task


class TaskListView(FilterView):
    template_name = "tasks/list.html"
    model = Task
    filterset_class = TaskFilter


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = "tasks/create.html"
    form_class = TaskCreateForm
    success_url = reverse_lazy("task_list")
    success_message = "Задача успешно создана"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class TaskChangeView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    template_name = "tasks/change.html"
    form_class = TaskCreateForm
    success_url = reverse_lazy("task_list")
    success_message = "Задача успешно изменена"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("task_list")
    template_name = "tasks/delete.html"
    success_message = "Задача успешно удалена"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            messages.error(request, "Задачу может удалить только её автор.")
            return redirect("task_list")
        return super(TaskDeleteView, self).dispatch(request, *args, **kwargs)


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/detail.html"
