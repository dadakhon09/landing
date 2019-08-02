from django.db import models
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
from django.db.models.signals import post_save
from django.dispatch import receiver


GENDER = (
    (0, 'Male'),
    (1, 'Female')
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    image = models.ImageField(blank=True, null=True, upload_to='media', default='profile.jpg')
    dob = models.DateField(blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    gender = models.IntegerField(choices=GENDER, blank=True, null=True)

    def __str__(self):
        self.get_gender_display()
        return self.user.username

@receiver(post_save, sender=User)
def wtf(sender, instance, **kwargs):
    userprofile = UserProfile.objects.get_or_create(user=instance)
