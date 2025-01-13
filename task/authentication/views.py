from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import User

class SignupView(APIView):
    def post(self, request):
        data = request.data
        if User.objects.filter(username=data['username']).exists():
            return Response({'message': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=data['username'],
            password=data['password']
        )
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        data = request.data
        user = User.objects.filter(username=data['username']).first()
        if user and user.check_password(data['password']):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

