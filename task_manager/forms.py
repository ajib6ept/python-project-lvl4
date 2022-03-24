from dataclasses import field
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Status


class TaskManagerUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(TaskManagerUserCreationForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs[
            "placeholder"
        ] = "Имя пользователя"
        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["first_name"].widget.attrs["placeholder"] = "Имя"
        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["placeholder"] = "Фамилия"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Пароль"
        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs[
            "placeholder"
        ] = "Подтверждение пароля"


class TaskManagerAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs[
            "placeholder"
        ] = "Имя пользователя"
        self.fields["password"].widget.attrs["class"] = "form-control"
        self.fields["password"].widget.attrs["placeholder"] = "Пароль"


class TaskManagerChangeUserForm(forms.ModelForm):

    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Пароль"
        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs[
            "placeholder"
        ] = "Подтверждение пароля"


class StatusCreateForm(ModelForm):
    class Meta:
        model = Status
        fields = ("name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["class"] = "form-control"
        self.fields["name"].widget.attrs["placeholder"] = "Имя"
