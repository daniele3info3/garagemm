# Generated by Django 4.1 on 2022-08-25 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_marca"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cor",
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
                ("nome", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "Cores",
            },
        ),
        migrations.CreateModel(
            name="Modelo",
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
                ("nome", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "Modelos",
            },
        ),
    ]
