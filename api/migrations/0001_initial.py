# Generated by Django 4.2 on 2024-06-04 05:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                (
                    "education",
                    models.CharField(
                        choices=[("B", "Bachelor"), ("M", "Master"), ("PH", "Phd")],
                        max_length=10,
                    ),
                ),
            ],
        ),
    ]
