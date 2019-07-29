import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from rest_framework import serializers
from django.conf import settings
from django.core.mail import EmailMessage

from mail.models import Startup

class StartupListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Startup
		fields = ('id', 'title', 'sender_name', 'sender_email', 'content', 'file','created_on')

class StartupCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Startup
		fields = ('title', 'sender_name', 'sender_email', 'content', 'file')

	def create(self, validated_data):
		s = Startup.objects.create(**validated_data)
		file = self.context['request'].FILES.get('file')
		s.file = file
		s.save()
		print(s.file)
		from_email = settings.EMAIL_HOST_USER
		recipient_list = ['odadaxon99@gmail.com',]
		subject = f'New Startup idea from {s.sender_name}'
		message = f' Title: {s.title} \n Sender email: {s.sender_email} \n Content: {s.content} \n'
		msg = EmailMessage(subject, message, from_email, recipient_list)
		msg.attach_file(os.path.join(BASE_DIR, f'{s.file}'))
		msg.send()
		return s
		