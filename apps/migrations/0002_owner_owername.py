# Generated by Django 5.1.1 on 2025-02-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apps", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="owner",
            name="OwerName",
            field=models.CharField(default="Devansh Durgapal", max_length=20),
        ),
    ]
