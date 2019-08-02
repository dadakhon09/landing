from django.urls import path
from userprofile.views import RegisterUser, UserLogin, UserLogout, GetProfile, UpdateProfile

urlpatterns = [
     path('register/', RegisterUser.as_view(), name='register'),
     path('login/', UserLogin.as_view(), name='login'),
     path('logout/', UserLogout.as_view(), name='logout'),
     #path('social_sign_up/', views.SocialSignUp.as_view(), name="social_sign_up"),
     path('profile/<int:id>/', GetProfile.as_view(), name='profile'),
     path('update/<int:id>/', UpdateProfile.as_view(), name='update'),
]
