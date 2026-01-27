from rest_framework import viewsets, permissions
from .models import Hotel
from .serializers import HotelSerializer

# 👇 ViewSet pour gérer les hotels
class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Sauvegarde l'utilisateur connecté comme créateur
        serializer.save(created_by=self.request.user)
