# Generated by Django 4.2.14 on 2024-07-17 20:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_child"),
    ]

    operations = [
        migrations.AddField(
            model_name="child",
            name="gender",
            field=models.CharField(default="Male", max_length=100),
        ),
    ]
