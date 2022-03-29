from django.forms import ModelForm

from .models import Task


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ("name", "description", "status", "worker")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["class"] = "form-control"
        self.fields["name"].widget.attrs["placeholder"] = "Имя"
        self.fields["description"].widget.attrs["class"] = "form-control"
        self.fields["description"].widget.attrs["placeholder"] = "Описание"
        self.fields["status"].widget.attrs["class"] = "form-control"
        self.fields["worker"].widget.attrs["class"] = "form-control"
