from django.db import models

class Startup(models.Model):
	title = models.CharField(max_length=255)
	sender_name = models.CharField(max_length=255)
	sender_email = models.EmailField(max_length=255)
	content = models.TextField()
	file = models.FileField(null=True, blank=True, upload_to="media")
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
