from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
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
        help = "Ваш пароль должен содержать как минимум 3 символа."
        self.fields["password1"].help_text = f"<ul><li>{help}</li></ul>"


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
    password1 = forms.CharField(
        widget=forms.PasswordInput(), label=_("Пароль")
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(), label=_("Подтверждение пароля")
    )

    class Meta:
        model = TaskUser
        fields = (
            "first_name",
            "last_name",
            "username",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        help = "Ваш пароль должен содержать как минимум 3 символа."
        self.fields["password1"].help_text = f"<ul><li>{help}</li></ul>"
        self.fields[
            "password2"
        ].help_text = "Для подтверждения введите, пожалуйста, пароль ещё раз."

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        try:
            validate_password(password1, self.instance)
        except forms.ValidationError as error:
            self.add_error("password1", error)

        try:
            validate_password(password2, self.instance)
        except forms.ValidationError as error:
            self.add_error("password2", error)

        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Введенные пароли не совпадают."))

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
