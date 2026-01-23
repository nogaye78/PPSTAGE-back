from django.urls import path
from .views import RegisterView # Remplace par le nom de ta vue

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]