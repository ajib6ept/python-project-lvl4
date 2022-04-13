from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, FormView, UpdateView
from django.views.generic.list import ListView

from .forms import LabelCreateForm
from .models import Label


class LabelListView(ListView):
    template_name = "labels/list.html"
    model = Label


class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = "labels/create.html"
    form_class = LabelCreateForm
    success_url = reverse_lazy("label_list")
    success_message = "Метка успешно создана"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LabelChangeView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    template_name = "labels/change.html"
    form_class = LabelCreateForm
    success_url = reverse_lazy("label_list")
    success_message = "Метка успешно изменена"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LabelDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Label
    success_url = reverse_lazy("label_list")
    template_name = "labels/delete.html"
    success_message = "Метка успешно удалена"
