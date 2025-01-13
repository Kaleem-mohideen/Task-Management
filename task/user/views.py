# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from django.core.files.storage import default_storage
import os
from .models import App, Task

# Create your views here.
class GetAppsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        apps = App.objects.all()
        return Response([{'id': app.id, 'name': app.name, 'points': app.points} for app in apps])

class UploadScreenshotView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self, request):
        user = request.user
        file = request.FILES.get('screenshot')
        if not file:
            return Response({'message': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        app_id = request.data.get('app_id')
        app = App.objects.filter(id=app_id).first()
        if not app:
            return Response({'message': 'App not found'}, status=status.HTTP_404_NOT_FOUND)

        file_path = default_storage.save(os.path.join('screenshots/', file.name), file)
        Task.objects.create(user=user, app=app, screenshot=file_path)
        return Response({'message': 'Screenshot uploaded successfully'}, status=status.HTTP_201_CREATED)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        tasks = Task.objects.filter(user=user)
        return Response({
            'username': user.username,
            'points': user.points,
            'tasks': [{'id': task.id, 'app_id': task.app.id, 'screenshot': task.screenshot.url} for task in tasks]
        })