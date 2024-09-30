from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from user.models import User
from rest_framework import status

class AuthViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])  # Burayı kontrol edin
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response({'error': 'Kullanıcı adı veya şifre yanlış.'}, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def user(self, request):
        print('hey')
        user = request.user

        user_data = {
            'id': user.id,
            'email': user.email,
            'name': user.get_full_name(),  
            'username': user.username,
        }

        return Response(user_data)
            