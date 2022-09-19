from django.contrib.auth.models import AbstractUser


class TaskUser(AbstractUser):
    def __str__(self):
        return self.get_full_name()

    @property
    def child_count(self):
        return self.task_author.count() + self.task_executor.count()
