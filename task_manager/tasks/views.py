from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, FormView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import TaskCreateForm
from .models import Task


class TaskListView(ListView):
    template_name = "tasks/list.html"
    model = Task


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = "tasks/create.html"
    form_class = TaskCreateForm
    success_url = reverse_lazy("task_list")
    success_message = "Your task was created successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class TaskChangeView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    template_name = "tasks/change.html"
    form_class = TaskCreateForm
    success_url = reverse_lazy("task_list")
    success_message = "Your task was changed successfully"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("task_list")
    template_name = "tasks/delete.html"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            messages.error(request, "Задачу может удалить только её автор.")
            return redirect("task_list")
        messages.success(request, "Задача удалена.")
        return super(TaskDeleteView, self).dispatch(request, *args, **kwargs)


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/detail.html"
