from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def child_count(self):
        return self.task_status.count()
