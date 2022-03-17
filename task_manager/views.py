from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.contrib.auth import login


from .forms import TaskManagerUserCreationForm, TaskManagerAuthenticationForm


class HomePageView(TemplateView):
    template_name = "home.html"


class UsersListView(ListView):
    template_name = "users_list.html"
    model = User


class UserCreateView(SuccessMessageMixin, FormView):
    template_name = "user_register.html"
    form_class = TaskManagerUserCreationForm
    success_url = reverse_lazy("user_login")
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserUpdateView(TemplateView):
    pass


class UserDeleteView(TemplateView):
    pass


class UserLoginView(SuccessMessageMixin, FormView):
    template_name = "user_login.html"
    success_url = reverse_lazy("home")
    form_class = TaskManagerAuthenticationForm
    success_message = "Successful login"

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("home")


# GET /users/ - страница со списком всех пользователей
# GET /users/create/ - страница регистрации нового пользователя (создание)
# POST /users/create/ - создание пользователя
# GET /users/<int:pk>/update/ - страница редактирования пользователя
# POST /users/<int:pk>/update/ - обновление пользователя
# GET /users/<int:pk>/delete/ - страница удаления пользователя
# POST /users/<int:pk>/delete/ - удаление пользователя
# GET /login/ - страница входа
# POST /login/ - аутентификация (вход)
# POST /logout/ - завершение сессии (выход)
