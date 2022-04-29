"""
Name: off chain
Author: Blas Moyano - Challenge Ripio - Copyright (C) 2022
Functionality: crytographys
"""

from cryptography.fernet import Fernet
from off_chain.settings.development import PRIVATE_KEY


class CustomCryptography:
    def __init__(self):
        self.fernet = Fernet(PRIVATE_KEY)

    def encrypt(self, data):
        return self.fernet.encrypt(data)

    def decrypt(self, token):
        return self.fernet.decrypt(token).decode()
