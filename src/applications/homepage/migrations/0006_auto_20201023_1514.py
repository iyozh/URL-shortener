# Generated by Django 3.1.2 on 2020-10-23 15:14

import storages.backends.s3boto3
from django.db import migrations, models

import applications.homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0005_qrcode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="qrcode",
            name="original",
            field=models.FileField(
                blank=True,
                null=True,
                storage=storages.backends.s3boto3.S3Boto3Storage(),
                upload_to=applications.homepage.models.upload_to,
            ),
        ),
    ]