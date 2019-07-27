from rest_framework import serializers
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
		print(self.context['request'].FILES)
		s.save()
		return s