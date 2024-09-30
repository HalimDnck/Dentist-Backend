# auth/serializers.py 

from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth import authenticate

User = get_user_model()  # Kullanıcı modelinizi alın

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        # Kullanıcıyı e-posta ile bul
        user = User.objects.filter(email=attrs['email']).first()

        if user is None:
            raise serializers.ValidationError('Kullanıcı adı veya şifre yanlış.')

        # Kullanıcıyı authenticate et
        user = authenticate(username=user.username, password=attrs['password'])

        if user is None:
            raise serializers.ValidationError('Kullanıcı adı veya şifre yanlış.')

        attrs['user'] = user
        return attrs
