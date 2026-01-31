from pathlib import Path
from decouple import config
import dj_database_url

# -----------------------
# BASE_DIR
# -----------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------
# SECRET / DEBUG / ALLOWED_HOSTS
# -----------------------
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS").split(",")

# -----------------------
# APPLICATIONS
# -----------------------
INSTALLED_APPS = [
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party apps
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "corsheaders",
    "cloudinary",
    "cloudinary_storage",
    "django_extensions",  # Pour show_urls

    # Custom apps
    "hotels",
]

# -----------------------
# MIDDLEWARE
# -----------------------
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# -----------------------
# URLS
# -----------------------
ROOT_URLCONF = "red_product_backend.urls"

# -----------------------
# TEMPLATES
# -----------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# -----------------------
# WSGI
# -----------------------
WSGI_APPLICATION = "red_product_backend.wsgi.application"

# -----------------------
# DATABASE (PostgreSQL)
# -----------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT", cast=int),
    }
}

# -----------------------
# AUTH USER
# -----------------------
AUTH_USER_MODEL = "hotels.CustomUser"

# -----------------------
# PASSWORD VALIDATION
# -----------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -----------------------
# INTERNATIONALIZATION
# -----------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Africa/Dakar"
USE_I18N = True
USE_TZ = True

# -----------------------
# STATIC & MEDIA
# -----------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# -----------------------
# REST FRAMEWORK
# -----------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
}

# -----------------------
# DJOSER (Activation Email + JWT)
# -----------------------
DJOSER = {
    "USER_ID_FIELD": "id",
    "LOGIN_FIELD": "email",
    "SERIALIZERS": {
        "user_create": "hotels.serializers.CustomUserCreateSerializer",
        "user": "hotels.serializers.CustomUserSerializer",
    },
    "TOKEN_MODEL": None,  # JWT utilisera SimpleJWT

    # Activation email
    "SEND_ACTIVATION_EMAIL": True,
    "ACTIVATION_URL": "http://localhost:5173/activate/{uid}/{token}/",  # Front dev
    "PASSWORD_RESET_CONFIRM_URL": "http://localhost:5173/reset-password/{uid}/{token}/",
}

# -----------------------
# EMAIL SMTP (Gmail pour vrai email)
# -----------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# -----------------------
# CORS
# -----------------------
CORS_ALLOWED_ORIGINS = config("CORS_ALLOWED_ORIGINS").split(",")

# -----------------------
# DEFAULT_AUTO_FIELD
# -----------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# source venv/Scripts/activate
# python manage.py runserver
