from django.forms import ModelForm

from .models import Status


class StatusCreateForm(ModelForm):
    class Meta:
        model = Status
        fields = ("name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["class"] = "form-control"
        self.fields["name"].widget.attrs["placeholder"] = "Имя"
