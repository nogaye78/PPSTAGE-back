from django.contrib import admin
from django.urls import path, include # N'oublie pas d'importer 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')), # Django va chercher dans accounts/urls.py
]