from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, FormView, UpdateView
from django.views.generic.list import ListView

from .forms import StatusCreateForm
from .models import Status


class StatusListView(LoginRequiredMixin, ListView):
    template_name = "statuses/list.html"
    model = Status


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = "statuses/create.html"
    form_class = StatusCreateForm
    success_url = reverse_lazy("status_list")
    success_message = "Статус успешно создан"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class StatusChangeView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    template_name = "statuses/change.html"
    form_class = StatusCreateForm
    success_url = reverse_lazy("status_list")
    success_message = "Статус успешно изменён"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class StatusDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    success_url = reverse_lazy("status_list")
    template_name = "statuses/delete.html"
    success_message = "Статус успешно удалён"
