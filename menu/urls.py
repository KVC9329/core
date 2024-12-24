from .views import RegisterView
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
]