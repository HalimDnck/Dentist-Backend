from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from core.base.views import BaseViewSet

class LoginViewSet(BaseViewSet):
  
    def create(self, request):
        # Kullanıcı bilgilerini al
        username = request.data.get('username')
        password = request.data.get('password')

        # Kullanıcıyı kimlik doğrulama işlemiyle kontrol et
        user = authenticate(username=username, password=password)
        
        if user:
            # Kullanıcıya token oluştur
            token, _ = Token.objects.get_or_create(user=user)
            return self.success_response({'token': token.key}, status_code=status.HTTP_200_OK)
        
        # Hatalı kimlik doğrulama durumunda hata döndür
        return self.error_response('Invalid Credentials', status_code=status.HTTP_401_UNAUTHORIZED)
