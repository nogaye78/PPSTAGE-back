from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet

router = DefaultRouter()
router.register(r'', HotelViewSet, basename='hotel')

urlpatterns = [
    path('', include(router.urls)),
]

# Les routes générées automatiquement seront :
# GET    /api/hotels/          → liste des hôtels
# POST   /api/hotels/          → créer un hôtel
# GET    /api/hotels/{id}/     → détail d'un hôtel
# PUT    /api/hotels/{id}/     → modifier un hôtel
# DELETE /api/hotels/{id}/     → supprimer un hôtel
# POST   /api/hotels/register/ → inscription
# POST   /api/hotels/login/    → connexion
# POST   /api/hotels/logout/   → déconnexion
# GET    /api/hotels/me/       → utilisateur connecté