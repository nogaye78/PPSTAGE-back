from rest_framework import viewsets, permissions
from .models import Hotel
from .serializers import HotelSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # <-- lecture publique, écriture protégée

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
