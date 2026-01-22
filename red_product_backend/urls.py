from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.views import RegisterView
from rest_framework.routers import DefaultRouter
from hotels.views import HotelViewSet

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view()),
    path('api/login/', TokenObtainPairView.as_view()), # C'est ici que tu récupères ton JWT
    path('api/', include(router.urls)),
] 

# Ajout crucial pour les images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)