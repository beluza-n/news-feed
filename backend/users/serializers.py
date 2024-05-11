from rest_framework import serializers
from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model


class CustomUserSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        fields = (
            'id',
            'email', 
            'username',
            'is_staff',
            )