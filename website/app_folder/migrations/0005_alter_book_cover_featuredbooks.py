# Generated by Django 5.1.1 on 2024-10-31 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_folder", "0004_rename_available_book_is_available"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="cover",
            field=models.ImageField(max_length=255, upload_to="covers/"),
        ),
        migrations.CreateModel(
            name="FeaturedBooks",
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
                ("order", models.PositiveIntegerField()),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_folder.book",
                    ),
                ),
            ],
        ),
    ]
