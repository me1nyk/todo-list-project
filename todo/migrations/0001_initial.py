# Generated by Django 4.1.7 on 2023-04-03 11:32

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("deadline", models.DateTimeField(blank=True, null=True)),
                ("is_done", models.BooleanField(default=False)),
                ("tags", models.ManyToManyField(related_name="tasks", to="todo.tag")),
            ],
            options={
                "ordering": ["-is_done", "-created_at"],
            },
        ),
    ]
