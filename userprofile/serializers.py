from rest_framework import serializers
from django.conf import settings
from django.contrib.auth.models import User
from userprofile.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'image', 'dob', 'occupation', 'gender', 'phone')


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'userprofile')
        read_only_fields = ('email', )


    