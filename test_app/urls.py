from django.urls import path

from test_app import views

urlpatterns = [
    path('pub/', views.test_img, name="test-img"),
    path('priv/', views.test_file, name="test-file"),
]
