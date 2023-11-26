# Generated by Django 4.2.5 on 2023-09-26 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("SystemMain", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SystemMainModel",
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
                ("firstname", models.CharField(max_length=255)),
                ("lastname", models.CharField(max_length=255)),
                ("phone", models.IntegerField(null=True)),
                ("joined_date", models.DateField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="SystemMain",
        ),
    ]
