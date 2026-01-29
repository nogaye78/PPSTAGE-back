from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import CustomUser

# Serializer pour création utilisateur
class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'password')

# Serializer pour afficher l'utilisateur
class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name')
