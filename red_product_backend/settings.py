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
DEBUG = config("DEBUG", cast=bool, default=True)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1,localhost").split(",")

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
    "django_extensions",

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
# DATABASE (Render compatible)
# -----------------------
DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
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
    "EXCEPTION_HANDLER": "hotels.utils.custom_exception_handler",
}

# -----------------------
# DJOSER (Activation + Reset)
# -----------------------
DOMAIN = "localhost:5173"
SITE_NAME = "PPSTAGE"

DJOSER = {
    "USER_ID_FIELD": "id",
    "LOGIN_FIELD": "email",
    "SERIALIZERS": {
        "user_create": "hotels.serializers.CustomUserCreateSerializer",
        "user": "hotels.serializers.CustomUserSerializer",
    },
    "SEND_ACTIVATION_EMAIL": True,
    "ACTIVATION_URL": "activate/{uid}/{token}/",
    "PASSWORD_RESET_CONFIRM_URL": "reset-password/{uid}/{token}/",
}

# -----------------------
# EMAIL (SMTP Gmail)
# -----------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# -----------------------
# CORS
# -----------------------
CORS_ALLOWED_ORIGINS = config("CORS_ALLOWED_ORIGINS", default="http://localhost:5173").split(",")

# -----------------------
# DEFAULT AUTO FIELD
# -----------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"







# source venv/Scripts/activate
# python manage.py runserver