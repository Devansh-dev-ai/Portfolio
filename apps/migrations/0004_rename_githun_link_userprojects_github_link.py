# Generated by Django 5.1.1 on 2025-02-27 18:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("apps", "0003_userprojects"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userprojects",
            old_name="githun_link",
            new_name="github_link",
        ),
    ]
