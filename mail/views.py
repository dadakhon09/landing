from django.shortcuts import render
from rest_framework import generics
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.views import View

from mail.serializers import StartupCreateSerializer, StartupListSerializer
from mail.models import Startup

def home(request):
	return render(request, 'home.html')

# class Sendmail(View):
# 	def post(self, request):
# 		print(request)
# 		return HttpResponse('Your message has been successfully sent')

# 	def get(self, request):
# 		subject = 'test title'
# 		message = 'something new'
# 		from_email = settings.EMAIL_HOST_USER
# 		recipient_list = ['odadaxon99@gmail.com','odadaxon27@mail.ru']
# 		send_mail(subject, message, from_email, recipient_list, fail_silently=False)
# 		return HttpResponse('Your message has been successfully sent')

class StartupCreateAPIView(generics.CreateAPIView):
	serializer_class = StartupCreateSerializer
	queryset = Startup.objects.all()


class StartupListAPIView(generics.ListAPIView):
	serializer_class = StartupListSerializer
	queryset = Startup.objects.all()

class StartupListWithIdAPIView(generics.ListAPIView):
	serializer_class = StartupListSerializer

	def get_queryset(self):
		id = self.kwargs['id']
		return Startup.objects.filter(id=id)


