# Generated by Django 3.1.2 on 2020-10-21 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0009_auto_20201021_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hit',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
