from django.http import HttpResponse

from test_app.models import Image, PrFile
from django_S3_minio_example.storage_backends import PrivateMediaStorage


def test_img(request):
    return HttpResponse([i.image.url for i in Image.objects.all()])


def test_file(request):
    private_storage = PrivateMediaStorage()
    urls = []
    for pr_file in PrFile.objects.all():
        if isinstance(pr_file.file.storage, PrivateMediaStorage):
            # Для приватных файлов генерируем подписанный URL
            url = private_storage.get_presigned_url(pr_file.file.name)
        else:
            # Для публичных файлов используем обычный URL
            url = pr_file.file.url
        urls.append(url)
    return HttpResponse(urls)
