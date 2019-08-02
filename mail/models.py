from django.db import models

class Startup(models.Model):
	title = models.CharField(max_length=255)
	sender_name = models.CharField(max_length=255)
	sender_email = models.EmailField(max_length=255)
	content = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Files(models.Model):
	file = models.FileField(upload_to='media', blank=True, null=True)
	startup = models.ForeignKey('Startup', on_delete=models.CASCADE, related_name='files')

	def __str__(self):
		return self.files
