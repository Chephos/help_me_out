from django.shortcuts import get_object_or_404

from . import models


class Video:
    @staticmethod
    def get_video_file_by_file_name(video_file_name: str):
        video_directory = "videos"
        video = get_object_or_404(
            models.Video, video_file=f"{video_directory}/{video_file_name}"
        )

        return video
