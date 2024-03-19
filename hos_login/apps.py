from django.apps import AppConfig


class HosLoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hos_login'
    AUTH_USER_MODEL = 'hos_login.User'
