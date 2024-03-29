from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class TaskUserAuthorizationMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj != self.request.user:
            message = _("У вас нет прав для изменения другого пользователя.")
            messages.error(request, message)
            return redirect("users_lists")
        return super().dispatch(request, *args, **kwargs)
