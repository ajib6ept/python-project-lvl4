import factory
from faker import Factory
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.labels.models import Label
from task_manager.users.models import TaskUser
from django.contrib.auth.hashers import make_password


faker = Factory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskUser

    # email = faker.email()

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Faker("email")
    password = factory.LazyFunction(lambda: make_password("pi3.1415"))


class StatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Status

    name = factory.Sequence(lambda n: "Status%s" % n)


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    name = factory.Sequence(lambda n: "Task%s" % n)
    description = faker.text()
    status = factory.SubFactory(StatusFactory)
    author = factory.SubFactory(UserFactory)
    worker = factory.SubFactory(UserFactory)


class LabelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Label

    name = factory.Sequence(lambda n: "Label%s" % n)
