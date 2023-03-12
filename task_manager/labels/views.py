from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import DeleteView, FormView, UpdateView
from django.views.generic.list import ListView

from task_manager.mixins import TaskManagerLoginRequiredMixin

from .forms import LabelCreateForm
from .models import Label


class LabelListView(TaskManagerLoginRequiredMixin, ListView):
    template_name = "labels/list.html"
    model = Label


class LabelCreateView(
    TaskManagerLoginRequiredMixin, SuccessMessageMixin, FormView
):
    template_name = "labels/create.html"
    form_class = LabelCreateForm
    success_url = reverse_lazy("label_list")
    success_message = _("Метка успешно создана")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LabelChangeView(
    TaskManagerLoginRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = Label
    template_name = "labels/change.html"
    form_class = LabelCreateForm
    success_url = reverse_lazy("label_list")
    success_message = _("Метка успешно изменена")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LabelDeleteView(
    TaskManagerLoginRequiredMixin, SuccessMessageMixin, DeleteView
):
    model = Label
    success_url = reverse_lazy("label_list")
    template_name = "labels/delete.html"
    success_message = _("Метка успешно удалена")

    def form_valid(self, form, *args, **kwargs):
        object = self.get_object()
        if object.child_count > 0:
            error_msg = _("Вы не можете удалить метку, связаннную с задачей")
            messages.error(self.request, error_msg)
            return HttpResponseRedirect(self.success_url)
        return super().form_valid(form)
