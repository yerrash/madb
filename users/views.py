from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView, Response, status

from .permissions import IsAdmin, IsUser
from .models import User
from .serializers import UserSerializer, LoginSerializer


class ListCreateUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUpdateUserView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsUser]
    serializer_class = UserSerializer


class LoginUserView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key})

        return Response(
            {"detail": "invalid email or password"}, status.HTTP_401_UNAUTHORIZED
        )
