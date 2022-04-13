from django.db import models
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import TaskUser


class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    author = models.ForeignKey(
        TaskUser, on_delete=models.CASCADE, related_name="author"
    )
    executor = models.ForeignKey(
        TaskUser, on_delete=models.CASCADE, related_name="executor"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    label = models.ManyToManyField(Label, blank=True)

    def __str__(self):
        return self.name
