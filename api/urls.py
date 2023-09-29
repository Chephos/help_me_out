from django.urls import path

from . import views

urlpatterns = [
    path("video/", views.Video.as_view(), name="save_video"),
    path("get-video/", views.Video.as_view(), name="get_video"),
]
