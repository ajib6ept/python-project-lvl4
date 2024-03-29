from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from task_manager.forms import TaskManagerAuthenticationForm


class HomePageView(TemplateView):
    template_name = "home.html"


class UserLoginView(SuccessMessageMixin, FormView):
    template_name = "users/login.html"
    success_url = reverse_lazy("home")
    form_class = TaskManagerAuthenticationForm
    success_message = _("Вы залогинены")

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

    def form_invalid(self, form):
        error_message = _(
            "Пожалуйста, введите правильные имя пользователя и пароль. \
            Оба поля могут быть чувствительны к регистру."
        )
        messages.error(self.request, error_message)
        return super().form_invalid(form)


class UserLogoutView(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "Вы разлогинены")
        return super().dispatch(request, *args, **kwargs)
