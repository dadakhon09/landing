from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAdminUser, AllowAny

from userprofile.serializers import UserSerializer, UserProfileSerializer
from userprofile.models import UserProfile

@permission_classes((AllowAny,))
class RegisterUser(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        first_name = data['first_name']
        last_name = data['last_name']
        mail = data['email']
        user_check = User.objects.filter(username=username)
        if not user_check:
            new_user = User.objects.create_user(username, mail, password)
            token, _ = Token.objects.get_or_create(user=new_user)
            new_user.first_name = first_name
            new_user.last_name = last_name

            new_user.save()
            return Response("User is created")
        else:
            return Response("We have already the same username")


@permission_classes((AllowAny,))
class UserLogin(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'})
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'})
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,
                         'user_id':user.id,
                         'username':user.username,
                         'status': user.is_superuser})

@permission_classes((AllowAny, IsAuthenticated))
class UserLogout(APIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        if request.user:
            print(request.user)
            request.user.auth_token.delete()
        else:

            Response("Please login first")
        return Response("Successfully logged out")        


class GetProfile(generics.ListAPIView):
    serializer_class = UserSerializer
    model = User
    #queryset = User.objects.get(id=id)

    def get_queryset(self):
        u = User.objects.filter(id=self.kwargs['id'])
        return u 

class UpdateProfile(generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = UserProfileSerializer
    model = UserProfile
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        u = UserProfile.objects.filter(id=self.kwargs['id'])
        return u

    def update(self, request, **kwargs):
        return super().update(request, **kwargs) 

    def perform_update(self, serializer):
        serializer.save()

        