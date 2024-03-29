# Generated by Django 4.1 on 2022-09-16 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tasks", "0005_alter_task_author_alter_task_executor_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="executor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="task_executor",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
