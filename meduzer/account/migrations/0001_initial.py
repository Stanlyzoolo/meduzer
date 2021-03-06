# Generated by Django 3.0.3 on 2020-03-01 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PlaceOfStudy",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("place", models.TextField(unique=True)),
            ],
            options={"verbose_name_plural": "place_of_study", "ordering": ["place"],},
        ),
        migrations.CreateModel(
            name="PlaceOfWork",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("work", models.TextField(unique=True)),
            ],
            options={"verbose_name_plural": "place_of_work",},
        ),
    ]
