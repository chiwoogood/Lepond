from django.conf import settings



def encrypt_data(data: str) -> bytes:
    return settings.FERNET.encrypt(data.encode())

def decrypt_data(token: bytes) -> str:
    return settings.FERNET.decrypt(token).decode()
