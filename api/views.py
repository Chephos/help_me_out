import os

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from . import helpers

# Create your views here.


class Video(APIView):
    def post(self, request):
        video_file = request.FILES.get("video_file")
        helpers.save_video_file_to_disk(video_file)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request):
        video_file_name = request.query_params.get("video_file_name")
        video_file = helpers.get_video_for_rendering(video_file_name)
        if video_file:
            # return render(request, "video.html", {"video_file": video_file})
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
