from django.forms import ModelForm

from .models import Label


class LabelCreateForm(ModelForm):
    class Meta:
        model = Label
        fields = ("name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["class"] = "form-control"
        self.fields["name"].widget.attrs["placeholder"] = "Имя"
