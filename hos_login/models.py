from django.db import models

# Create your models here.
from django.db import models
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken




SECRET_KEY = b'xaSv9SyMXgUgm_Q0kBnC0uSuVPxbxTsnZlRhpz27pBQ='
cipher_suite = Fernet(SECRET_KEY)

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed
    def __str__(self):
        return self.name
class User(models.Model):
    hospital = models.CharField(max_length=100, default=None)
    username = models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    encrypted_password = models.BinaryField()
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
