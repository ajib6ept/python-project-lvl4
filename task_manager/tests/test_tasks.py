from django.test import Client, TestCase
from django.urls import reverse
from task_manager.tasks.models import Task, TaskUser, Label

from task_manager.tests.factories import (
    LabelFactory,
    StatusFactory,
    TaskFactory,
    UserFactory,
    Status,
)


class TaskCreateChangeDeleteTest(TestCase):
    def setUp(self):
        self.author = UserFactory()
        self.executor = UserFactory()
        self.status = StatusFactory()
        self.label = LabelFactory()
        self.task = TaskFactory.build()
        self.client = Client()
        self.client.force_login(self.author)
        self.client_without_auth = Client()

    def from_task_factory_item_to_dict(self, item):
        return {
            "name": item.name,
            "description": item.description,
            "status": self.status.pk,
            "executor": self.executor.pk,
            "label": self.label.pk,
        }

    def test_create_task(self):
        new_task_dict = self.from_task_factory_item_to_dict(self.task)
        self.client_without_auth.post(reverse("task_create"), new_task_dict)
        self.assertEqual(
            Task.objects.filter(name=new_task_dict["name"]).exists(),
            False,
        )
        self.client.post(reverse("task_create"), new_task_dict)
        self.assertEqual(
            Task.objects.filter(name=new_task_dict["name"]).exists(),
            True,
        )

    def test_change_task(self):
        change_task = TaskFactory()
        change_task_dict = self.from_task_factory_item_to_dict(change_task)
        new_task_name = TaskFactory.build().name
        self.assertNotEqual(change_task_dict["name"], new_task_name)
        change_task_dict["name"] = new_task_name
        self.client_without_auth.post(
            reverse("task_chd", kwargs={"pk": change_task.pk}),
            change_task_dict,
        )
        self.assertEqual(
            Task.objects.filter(name=change_task_dict["name"]).exists(),
            False,
        )
        self.client.post(
            reverse("task_chd", kwargs={"pk": change_task.pk}),
            change_task_dict,
        )
        self.assertEqual(
            Task.objects.filter(name=change_task_dict["name"]).exists(),
            True,
        )

    def test_delete_status(self):
        delete_task = TaskFactory(author=self.author)
        self.client_without_auth.post(
            reverse("task_del", kwargs={"pk": delete_task.pk})
        )
        self.assertEqual(
            Task.objects.filter(name=delete_task.name).exists(),
            True,
        )
        other_author = UserFactory()
        other_client = Client()
        other_client.force_login(other_author)
        other_client.post(reverse("task_del", kwargs={"pk": delete_task.pk}))
        self.assertEqual(
            Task.objects.filter(name=delete_task.name).exists(),
            True,
        )
        self.client.post(reverse("task_del", kwargs={"pk": delete_task.pk}))
        self.assertEqual(
            Task.objects.filter(name=delete_task.name).exists(),
            False,
        )

    def test_delete_status_attributes(self):
        """
        Prohibit deleting a label, status, user
        if there is a task associated with them
        """
        task = TaskFactory.create(labels=[LabelFactory(), LabelFactory()])
        task_author = task.author
        task_executor = task.executor
        task_status = task.status
        task_label = task.labels.all()[0]

        client = Client()
        client.force_login(task_author)

        client.post(reverse("user_del", kwargs={"pk": task_executor.pk}))
        self.assertEqual(
            TaskUser.objects.filter(username=task_author.username).exists(),
            True,
        )

        client.post(reverse("user_del", kwargs={"pk": task_executor.pk}))
        self.assertEqual(
            TaskUser.objects.filter(username=task_executor.username).exists(),
            True,
        )

        client.post(reverse("status_del", kwargs={"pk": task_status.pk}))
        self.assertEqual(
            Status.objects.filter(name=task_status.name).exists(),
            True,
        )

        client.post(reverse("label_del", kwargs={"pk": task_label.pk}))
        self.assertEqual(
            Label.objects.filter(name=task_label.name).exists(),
            True,
        )
