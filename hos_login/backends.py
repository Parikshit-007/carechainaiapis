from django.contrib.auth.backends import ModelBackend
from .models import Custom_User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class CustomUserModelBackend(ModelBackend):
    @method_decorator(csrf_exempt)
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Custom_User.objects.get(username=username)
            if user.check_password(password):
                return user
        except Custom_User.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return Custom_User.objects.get(pk=user_id)
        except Custom_User.DoesNotExist:
            return None    
    # @property
    # def last_login(self):
    #     # Override last_login attribute to avoid the error
    #     return None    