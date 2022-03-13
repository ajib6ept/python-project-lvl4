from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = "home.html"


class UsersListView(ListView):
    template_name = "users_list.html"
    model = User


class UserCreateView(FormView):
    template_name = "user_create.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("home")


class UserUpdateView(TemplateView):
    pass


class UserDeleteView(TemplateView):
    pass


class UserLoginView(TemplateView):
    pass


class UserLogoutView(TemplateView):
    pass


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
