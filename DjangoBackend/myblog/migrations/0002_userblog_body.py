# Generated by Django 5.0.1 on 2024-02-02 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myblog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userblog",
            name="body",
            field=models.TextField(default=""),
        ),
    ]
