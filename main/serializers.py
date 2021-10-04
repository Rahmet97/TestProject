from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Users, New


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'
