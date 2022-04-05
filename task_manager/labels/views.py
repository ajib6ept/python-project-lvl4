from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, FormView, UpdateView
from django.views.generic.list import ListView

from .models import Label
from .forms import LabelCreateForm


class LabelListView(ListView):
    template_name = "labels/list.html"
    model = Label


class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = "labels/create.html"
    form_class = LabelCreateForm
    success_url = reverse_lazy("label_list")
    success_message = "Your label was created successfully"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LabelChangeView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    template_name = "labels/change.html"
    form_class = LabelCreateForm
    success_url = reverse_lazy("label_list")
    success_message = "Your label was changed successfully"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    success_url = reverse_lazy("label_list")
    template_name = "labels/delete.html"
