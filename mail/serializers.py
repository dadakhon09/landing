import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from rest_framework import serializers
from django.conf import settings
from django.core.mail import EmailMessage

from mail.models import Startup, Files

class FilesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Files
		fields = ('id', 'file')

class StartupListSerializer(serializers.ModelSerializer):
	files = FilesSerializer(many=True)
	class Meta:
		model = Startup
		fields = ('id', 'title', 'sender_name', 'sender_email', 'content', 'files','created_on')

class StartupCreateSerializer(serializers.ModelSerializer):
	# files = FilesSerializer(many=True)
	class Meta:
		model = Startup
		fields = ('title', 'sender_name', 'sender_email', 'content')

 
	def create(self, validated_data):
		s = Startup.objects.create(**validated_data)
		# files = list( self.context['request'].FILES.values() )
		# print(files)
		# print(self.context['request'].FILES.values())
		# files_serializer = FilesSerializer( data={"files": files} )
		files_list = []
		files = self.context['request'].FILES.getlist('files')
		if files:
			for f in files:
				print(f)
				fil = Files.objects.create(file=f, startup=s)
				files_list.append(fil.file)
				#files_list.append(Files.objects.create(file=f, startup=s))
		s.save()
		print(files)
		from_email = settings.EMAIL_HOST_USER
		recipient_list = ['odadaxon99@gmail.com',]
		subject = f'New Startup idea from {s.sender_name}'
		message = f' Title: {s.title} \n Sender email: {s.sender_email} \n Content: {s.content} \n'
		msg = EmailMessage(subject, message, from_email, recipient_list)
		print(files_list)
		for f in files_list:
			print(f)
			msg.attach_file(os.path.join(BASE_DIR, f.name))
		msg.send()
		return s


	# def update(self, s, validated_data):
	# 	request = self.context['request']
	# 	files = request.FILES.getlist('files')
	# 	if files:
	# 		for i in files:
	# 			Files.objects.create(file=i, startup=s)
	# 	return super().update(s, validated_data)
	# 	