from rest_framework import serializers

from . import models

class Video(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = ("video_file",)