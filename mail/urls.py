from django.urls import path
from .views import home, StartupListAPIView, StartupCreateAPIView, StartupListWithIdAPIView

urlpatterns = [
	path('', home, name='home'),
	path('startup/create/', StartupCreateAPIView.as_view(), name='startup-create'),
	path('startup/list/', StartupListAPIView.as_view(), name='startup-list'),
	path('startup/list/<int:id>/', StartupListWithIdAPIView.as_view(), name='startup-list-with-id'),
]