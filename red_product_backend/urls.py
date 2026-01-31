# red_product_backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # CRUD Hotels
    path('api/hotels/', include('hotels.urls')),

    # Authentification Djoser
    path('api/auth/', include('djoser.urls')),          # endpoints inscription, mot de passe, user info
    path('api/auth/', include('djoser.urls.jwt')),      # endpoints JWT (create, refresh, verify)
]
