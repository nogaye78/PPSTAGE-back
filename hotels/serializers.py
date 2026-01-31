from rest_framework import serializers
from .models import Hotel, CustomUser  # Assure-toi que CustomUser est bien importé

# --- Serializer pour CustomUser (affichage) ---
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name']  # adapte selon ton modèle

# --- Serializer pour CustomUser lors de la création ---
class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user

# --- Serializer pour Hotel ---
class HotelSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)

    class Meta:
        model = Hotel
        fields = '__all__'
