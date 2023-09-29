import os

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from . import helpers, workers
from . import serializers

# Create your views here.


class Video(APIView):
    def post(self, request):
        serializer = serializers.Video(data=request.FILES)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request):
        video_file_name = request.query_params.get("video_file_name")
        video_file = workers.Video.get_video_file_by_file_name(video_file_name)
        # TODO: render video in template
        return Response(status=status.HTTP_200_OK)
