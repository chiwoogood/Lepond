from cryptography.fernet import Fernet
from django.conf import settings

cipher = Fernet(settings.ENCRYPTION_KEY)

def encrypt_data(data: str) -> str:
    return cipher.encrypt(data.encode()).decode()

def decrypt_data(token: str) -> str:
    return cipher.decrypt(token.encode()).decode()
