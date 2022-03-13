from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class HomePageView(TemplateView):
    template_name = "home.html"


class UsersListView(ListView):
    template_name = "users_list.html"
    model = User


class UserCreateView(SuccessMessageMixin, FormView):
    template_name = "user_register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("home")
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


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
