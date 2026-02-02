from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        # Cas d’erreur login (email inexistant ou mauvais mot de passe)
        if response.status_code == 400:
            if "non_field_errors" in response.data:
                response.data = {"error": "Adresse email ou mot de passe incorrect."}
        elif response.status_code == 401:
            response.data = {"error": "Compte inactif ou non trouvé."}

    return response
