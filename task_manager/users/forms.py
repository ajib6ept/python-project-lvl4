from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

from task_manager.users.models import TaskUser


class TaskManagerUserCreationForm(UserCreationForm):

    class Meta:
        model = TaskUser
        fields = (
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
        )


    def __init__(self, *args, **kwargs):
        super(TaskManagerUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = '<ul><li>Ваш пароль должен содержать как минимум 3 символа.</li></ul>'



class TaskManagerAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = _(
            "Имя пользователя"
        )
        self.fields["password"].widget.attrs["class"] = "form-control"
        self.fields["password"].widget.attrs["placeholder"] = _("Пароль")


class TaskManagerChangeUserForm(forms.ModelForm):

    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = TaskUser
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
        self.fields["password1"].widget.attrs["placeholder"] = _("Пароль")
        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = _(
            "Подтверждение пароля"
        )
