# Generated by Django 4.1.2 on 2022-10-29 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Advocate",
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
                (
                    "profile_pic",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("username", models.CharField(max_length=200)),
                ("name", models.CharField(max_length=100)),
                ("twitter", models.CharField(max_length=60)),
                ("bio", models.TextField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]