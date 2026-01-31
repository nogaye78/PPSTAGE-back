from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet

router = DefaultRouter()
router.register(r'', HotelViewSet, basename='hotel')  # endpoint principal pour /hotels/

urlpatterns = [
    path('', include(router.urls)),
]
