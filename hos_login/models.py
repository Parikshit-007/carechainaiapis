from django.db import models

# Create your models here.
from django.db import models
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User as BaseUser
from django.contrib.auth.models import AbstractUser, Group, Permission

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email is not given.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff = True")

        if not extra_fields.get('is_superuser'): 
            raise ValueError("Superuser must have is_superuser = True")
        return self.create_user(email, password, **extra_fields)




SECRET_KEY = b'xaSv9SyMXgUgm_Q0kBnC0uSuVPxbxTsnZlRhpz27pBQ='
cipher_suite = Fernet(SECRET_KEY)

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed
    def __str__(self):
        return self.name
class Custom_User(AbstractBaseUser):
    #hospital = models.CharField(max_length=100, default=None)
    username = models.CharField(max_length=100, unique=True)
    email=models.EmailField(max_length=100)
    encrypted_password = models.BinaryField()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    last_login = models.DateTimeField(auto_now=True, null=True)
    USERNAME_FIELD = 'username'
  # Add this field
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True
    # Add other fields as needed

    def set_password(self, password):
        # Encrypt the password before saving it to the database
        self.encrypted_password = cipher_suite.encrypt(password.encode())

    def check_password(self, password):
        try:
            # Decrypt the stored password and compare it with the entered password
            decrypted_password = cipher_suite.decrypt(self.encrypted_password).decode()
            return password == decrypted_password
        except InvalidToken:
            # Handle InvalidToken exception, return False for invalid tokens
            return False
    def update_last_login(self, *args, **kwargs):
        # Override the signal handler to prevent updating last_login
        pass    
    # def save(self, *args, **kwargs):
    #     # Set a default password and encrypt it before saving
    #     if not self.pk:  # Only set the default password if this is a new user
    #         default_password = self.encrypted_password  # You can set any default password here
    #         self.set_password(default_password)
    #     super().save(*args, **kwargs)    
    # groups = models.ManyToManyField(
    #     Group,
    #     verbose_name='groups',
    #     blank=True,
    #     related_name='hos_login_users_groups'  # Unique related name
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     verbose_name='user permissions',
    #     blank=True,
    #     related_name='hos_login_users_permissions'  # Unique related name
    # )