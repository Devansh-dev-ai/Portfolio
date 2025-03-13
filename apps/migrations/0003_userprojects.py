# Generated by Django 5.1.1 on 2025-02-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apps", "0002_owner_owername"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProjects",
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
                ("name", models.CharField(max_length=15)),
                ("description", models.CharField(max_length=50)),
                ("githun_link", models.URLField()),
                (
                    "project_picture",
                    models.ImageField(upload_to="image/ProjectsImages"),
                ),
            ],
        ),
    ]
