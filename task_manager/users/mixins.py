from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskUserAuthorizationMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj != self.request.user:
            messages.error(
                request, "У вас нет прав для изменения другого пользователя."
            )
            return redirect("users_lists")
        return super().dispatch(request, *args, **kwargs)
