from tonpy.libs.python_ton import PyMnemonic, create_new_mnemo, PyPrivateKey, PyPublicKey
from tonpy.libs.python_ton import get_bip39_words as c_get_bip39_words
from typing import List


def get_bip39_words():
    return c_get_bip39_words()


# ED25519
class PublicKey:
    def __init__(self, public_key_hex: str = None,
                 key: PyPublicKey = None):
        if key is not None:
            self.key = key
        else:
            self.key = PyPublicKey(public_key_hex)

    def to_hex(self):
        return self.key.get_public_key_hex().zfill(64)


class PrivateKey:
    def __init__(self, private_key_hex: str = None, key: PyPrivateKey = None):
        if private_key_hex:
            assert len(private_key_hex) == 64
            self.key = PyPrivateKey(bytearray.fromhex(private_key_hex)[::-1].hex())
        elif key is not None:
            self.key = key
        else:
            self.key = PyPrivateKey()

    def to_hex(self):
        return self.key.get_private_key_hex().zfill(64)

    def get_public_key(self) -> PublicKey:
        return PublicKey(key=self.key.get_public_key())


class Mnemonic:
    def __init__(self, words: List[str] = None,
                 password='',
                 entropy='',
                 words_count=24):
        """
        Create new mnemonic from entropy, password, words_count or  export from words, password

        :param words:
        :param password:
        :param words_count:
        """

        if words is None:
            self.mnemo = create_new_mnemo(entropy, password, words_count)
        else:
            self.mnemo = PyMnemonic(words, password)

    def get_words(self) -> List[str]:
        return self.mnemo.get_words()

    def get_private_key_hex(self) -> str:
        return self.mnemo.get_private_key_hex()

    def get_private_key(self) -> PrivateKey:
        return PrivateKey(key=self.mnemo.get_private_key())
