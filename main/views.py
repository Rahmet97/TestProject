from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from main.models import Users
from main.serializers import UsersSerializer, UserSerializer


class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


@api_view(['post'])
@authentication_classes([])
@permission_classes([])
def sign_up(request):
    try:
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        username = request.data.get('username')
        email = request.data.get('email')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                data = {
                    "success": False,
                    "message": "Bunday foydalanuvchi mavjud"
                }
                return Response(data, status=405)
            else:
                us = User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email, password=make_password(password1))
                us.save()
                data = {
                    "success": True,
                    "message": "Welcome!!!"
                }
        else:
            data = {
                "success": False,
                "message": "Parollar to'g'ri kelmadi!!!"
            }
            return Response(data, status=405)
    except:
        data = {
            "success": False,
            "message": "Xatolik!!!"
        }
        return Response(data, status=405)
    return Response(data, status=200)


@api_view(['post'])
@authentication_classes([])
@permission_classes([])
def login(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        us = User.objects.get(username=username)
        if check_password(password, us.password):
            user = UserSerializer(us)
            token = RefreshToken.for_user(us)
            tk = {
                "refresh": str(token),
                "access": str(token.access_token)
            }
            data = {
                "success": True,
                "message": "Kirish tasdiqlandi",
                "data": {
                    "user": user.data,
                    "token": tk
                }
            }
        else:
            data = {
                "success": False,
                "message": "Username yoki parol xato!!!"
            }
            return Response(data, status=405)
    except:
        data = {
            "success": False,
            "message": "Xatolik!!!"
        }
        return Response(data, status=405)
    return Response(data, status=200)
