import django_filters
from django import forms

from task_manager.labels.models import Label

from .models import Task


class TaskFilter(django_filters.FilterSet):
    labels = django_filters.ModelChoiceFilter(queryset=Label.objects.all())
    self_tasks = django_filters.BooleanFilter(
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
        method="self_task",
    )

    def self_task(self, queryset, *args, **kwargs):
        if args:
            self_user_filter = args[1]
            if self_user_filter:
                return queryset.filter(author=self.request.user.pk)
        return queryset

    class Meta:
        model = Task
        fields = ["status", "executor", "labels"]
