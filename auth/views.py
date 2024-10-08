from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from user.models import User
from rest_framework import status

class AuthViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def user(self, request):
        user = request.user

        user_data = {
            'id': user.id,
            'email': user.email,
            'name': user.name,  
            'username': user.username,
        }

        return Response(user_data)
            