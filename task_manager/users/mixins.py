from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _


class TaskUserAuthorizationMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj != self.request.user:
            message = _("Вы не авторизованы! Пожалуйста, выполните вход.")
            messages.error(request, message)
            return redirect("user_login")
        return super().dispatch(request, *args, **kwargs)
