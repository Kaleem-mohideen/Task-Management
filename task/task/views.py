
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from user.models import App

class AddAppView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        data = request.data
        app = App.objects.create(name=data['name'], points=data['points'])
        return Response({'message': 'App added successfully'}, status=status.HTTP_201_CREATED)
