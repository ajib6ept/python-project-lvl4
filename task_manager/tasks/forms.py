from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Task


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ("name", "description", "status", "executor", "labels")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["class"] = "form-control"
        self.fields["name"].widget.attrs["placeholder"] = _("Имя")
        self.fields["description"].widget.attrs["class"] = "form-control"
        self.fields["description"].widget.attrs["placeholder"] = _("Описание")
        self.fields["status"].widget.attrs["class"] = "form-control"
        self.fields["executor"].widget.attrs["class"] = "form-control"
        self.fields["labels"].widget.attrs["class"] = "form-control"
