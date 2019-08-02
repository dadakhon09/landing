from django.shortcuts import render
from rest_framework import generics
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.views import View
from rest_framework.response import Response

from mail.serializers import StartupCreateSerializer, StartupListSerializer
from mail.models import Startup

def home(request):
	return render(request, 'home.html')

class StartupCreateAPIView(generics.CreateAPIView):
    serializer_class = StartupCreateSerializer
    queryset = Startup.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = StartupListSerializer(serializer.instance)
        return Response(data.data, status=201, headers=headers)


class StartupListAPIView(generics.ListAPIView):
	serializer_class = StartupListSerializer
	queryset = Startup.objects.all()

class StartupListWithIdAPIView(generics.ListAPIView):
	serializer_class = StartupListSerializer

	def get_queryset(self):
		id = self.kwargs['id']
		return Startup.objects.filter(id=id)


