import pytest
from balance.utils.cryptographys import CustomCryptography


@pytest.mark.hash
def test_custom_cryptography():
    DATA = "test"
    encrypt = CustomCryptography().encrypt(bytes(DATA, encoding="utf8"))
    decrypt = CustomCryptography().decrypt(encrypt)
    assert decrypt == DATA
