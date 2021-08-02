# Generated by Django 3.1.2 on 2020-10-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Url",
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
                ("original", models.URLField(blank=True, null=True)),
                ("shortcut", models.URLField(blank=True, null=True)),
            ],
        ),
    ]
