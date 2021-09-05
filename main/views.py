from rest_framework import generics
from main.models import Users
from main.serializers import UsersSerializer


class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
