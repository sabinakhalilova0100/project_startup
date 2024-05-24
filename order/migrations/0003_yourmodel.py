# Generated by Django 4.1.3 on 2024-05-21 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="YourModel",
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
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=15)),
                ("random_number", models.IntegerField()),
            ],
        ),
    ]
