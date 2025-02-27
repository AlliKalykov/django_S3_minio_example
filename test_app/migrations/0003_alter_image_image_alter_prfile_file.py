# Generated by Django 5.0.1 on 2024-03-25 12:20

import django_S3_minio_example.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_prfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(storage=django_S3_minio_example.storage_backends.PublicMediaStorage(), upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='prfile',
            name='file',
            field=models.FileField(storage=django_S3_minio_example.storage_backends.PrivateMediaStorage(), upload_to='files/'),
        ),
    ]
