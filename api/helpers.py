import os

from django.conf import settings
from django.http import FileResponse


def save_video_file_to_disk(video_file):
    file_path = os.path.join(settings.MEDIA_ROOT, "videos", video_file.name)

    with open(file_path, "wb+") as destination:
        for chunk in video_file.chunks():
            destination.write(chunk)


def get_video_for_rendering(video_file_name: str):
    video_file_path = os.path.join(settings.MEDIA_ROOT, "videos", video_file_name)

    if not os.path.exists(video_file_path):
        return None
    response = FileResponse(open(video_file_path, "rb"))
    return response
