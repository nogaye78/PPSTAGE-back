from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

# Endpoint test CSRF
def csrf(request):
    return JsonResponse({"detail": "CSRF cookie set"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),         # endpoints inscription, activation...
    path('api/auth/', include('djoser.urls.jwt')),     # endpoints JWT login/logout
    path('api/hotels/', include('hotels.urls')),       # tes endpoints hôtels
    path('api/csrf/', ensure_csrf_cookie(csrf)),      # test CSRF
]
