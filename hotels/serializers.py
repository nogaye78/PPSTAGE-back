from rest_framework import serializers
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    # Champ calculé pour afficher le nom de l'utilisateur au lieu de son ID
    created_by_username = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'address', 'price', 'image', 'created_by', 'created_by_username']
        # L'utilisateur connecté est assigné automatiquement, donc c'est en lecture seule
        read_only_fields = ['created_by']