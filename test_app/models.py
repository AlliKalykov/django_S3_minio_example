from django.db import models
from django_S3_minio_example.storage_backends import PrivateMediaStorage, PublicMediaStorage


class Image(models.Model):
    image = models.ImageField(storage=PublicMediaStorage(), upload_to='images/')


class PrFile(models.Model):
    file = models.FileField(storage=PrivateMediaStorage(), upload_to='files/')
