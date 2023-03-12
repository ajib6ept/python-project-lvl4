from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class TaskManagerLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy("user_login")
    redirect_field_name = "redirect_to"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            error_msg = _("Вы не авторизованы! Пожалуйста, выполните вход.")
            messages.error(request, error_msg)
        return super().dispatch(request, *args, **kwargs)
