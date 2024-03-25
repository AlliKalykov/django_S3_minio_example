import boto3
from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'


class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False


class PrivateMediaStorage(S3Boto3Storage):
    location = 'private'
    bucket_name = 'example'
    default_acl = 'private'
    custom_domain = False

    def get_presigned_url(self, name, expires_in=3600):
        """
        Генерирует подписанный URL для доступа к приватному файлу в MinIO.
        """
        s3_client = boto3.client('s3',
                                 region_name=settings.AWS_S3_REGION_NAME,
                                 endpoint_url=settings.AWS_S3_ENDPOINT_URL,
                                 aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                                 config=boto3.session.Config(signature_version='s3v4'),
                                 verify=settings.AWS_S3_USE_SSL)
        presigned_url = s3_client.generate_presigned_url('get_object',
                                                         Params={'Bucket': self.bucket_name,
                                                                 'Key': f"{self.location}/{name}"},
                                                         ExpiresIn=expires_in)
        return presigned_url
