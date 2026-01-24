from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.models import User
from django.core.mail import send_mail

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if not username or not email or not password:
            return Response({"error": "Tous les champs sont obligatoires."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Ce nom d'utilisateur existe déjà."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)

        # 📧 Envoi de l’email de bienvenue
        send_mail(
            subject="Bienvenue sur Red Product 🎉",
            message=f"Bonjour {username},\n\nVotre compte a été créé avec succès.\n\nBienvenue sur Red Product !",
            from_email=None,  # utilisera DEFAULT_FROM_EMAIL
            recipient_list=[email],
            fail_silently=False,
        )

        return Response(
            {"message": "Compte créé avec succès ! Un email de bienvenue a été envoyé 📧"},
            status=status.HTTP_201_CREATED
        )
