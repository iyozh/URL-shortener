# Generated by Django 3.1.2 on 2020-10-18 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("statistics", "0002_auto_20201018_2127"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hit",
            name="browser",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
