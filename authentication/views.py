
import requests
from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class AddUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  # Allows unauthenticated users to access this view


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['Password'] = user.password
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


UID = "u-s4t2ud-4668a395508c9efad23fa632aa46cdc6272d8fb858f911fc4af32e575a1e3e8f"
SECRET = "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"

class OAuth2CallbackView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        code = request.query_params.get('code')
        token_url = "https://api.intra.42.fr/oauth/token"
        data = {
            'grant_type': 'authorization_code',
            'client_id': UID,
            'client_secret': SECRET,
            'code': code,
            'redirect_uri': "http://localhost:8000/api/callback",
        }
        response = requests.post(token_url, data=data)
        print(response.json())
        access_token = response.json().get('access_token')

        user_info_url = "https://api.intra.42.fr/v2/me"
        headers = {'Authorization': f'Bearer {access_token}'}
        user_info = requests.get(user_info_url, headers=headers).json()

        status = user_info.get('status', None)
        if status is not None:
            return Response(user_info)

        user, created = User.objects.get_or_create(username=user_info['login'])

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.id,
            'username': user.username,
        })
