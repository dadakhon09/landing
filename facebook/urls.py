from django.urls import path
from facebook.facebook import fb

urlpatterns = [
    path('', fb),
]