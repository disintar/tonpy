from tonpy.libs.python_ton import PyMnemonic, create_new_mnemo, PyPrivateKey, PyPublicKey
from tonpy.libs.python_ton import get_bip39_words as c_get_bip39_words
from typing import List, Union

def get_bip39_words() -> List[str]:
    """
    Return the BIP-39 word list bundled with the native library.

    Returns:
        List[str]: The standard BIP-39 English word list.
    """
    return c_get_bip39_words()


# ED25519
class PublicKey:
    """ED25519 public key helper.

    You can construct it from a hex-encoded public key or from a native PyPublicKey.
    """
    def __init__(self, public_key_hex: str = None,
                 key: PyPublicKey = None):
        """
        Args:
            public_key_hex: 32-byte ED25519 public key hex string (without 0x, 64 hex chars).
            key: Existing native key instance.
        """
        if key is not None:
            self.key = key
        else:
            self.key = PyPublicKey(public_key_hex)

    def to_hex(self) -> str:
        """Return hex string for the public key (zero-padded to 64 chars)."""
        return self.key.get_public_key_hex().zfill(64)

    def verify_signature(self, data: bytes, signature: bytes, raise_on_error=True) -> bool:
        """
        Verify ED25519 signature.

        Args:
            data: Original message bytes or hex string.
            signature: Signature bytes.
            raise_on_error: If True, raise ValueError on verification failure.

        Returns:
            bool: True if signature is valid, False otherwise (when raise_on_error=False).
        """
        if isinstance(data, str):
            data = bytes.fromhex(data)

        result, err_msg = self.key.verify_signature(data, signature)

        if not result and raise_on_error:
            raise ValueError(err_msg)

        return result


class PrivateKey:
    """ED25519 private key helper with signing and public key derivation."""
    def __init__(self, private_key_hex: str = None, key: PyPrivateKey = None):
        """
        Args:
            private_key_hex: 32-byte ED25519 private key hex string (64 hex chars). If provided, will be endian-adjusted for the native library.
            key: Existing native key instance.
        """
        if private_key_hex:
            assert len(private_key_hex) == 64
            self.key = PyPrivateKey(bytearray.fromhex(private_key_hex)[::-1].hex())
        elif key is not None:
            self.key = key
        else:
            self.key = PyPrivateKey()

    def to_hex(self) -> str:
        """Return hex string for the private key (zero-padded to 64 chars)."""
        return self.key.get_private_key_hex().zfill(64)

    def get_public_key(self) -> PublicKey:
        """Derive the corresponding ED25519 PublicKey."""
        return PublicKey(key=self.key.get_public_key())

    def sign(self, data: Union[bytes, str]) -> bytes:
        """
        Sign data with the private key.

        Args:
            data: Message bytes or hex string to sign.

        Returns:
            bytes: Signature (64 bytes)
        """
        if isinstance(data, str):
            data = bytes.fromhex(data)

        return self.key.sign(data)[:64]


class Mnemonic:
    """BIP-39 mnemonic utilities for key derivation."""
    def __init__(self, words: List[str] = None,
                 password: str = '',
                 entropy: str = '',
                 words_count: int = 24):
        """
        Create a new mnemonic or import from an existing word list.

        Args:
            words: Existing mnemonic words. If None, a new mnemonic will be generated from entropy.
            password: Optional mnemonic password (passphrase).
            entropy: Optional entropy hex string to generate mnemonic from.
            words_count: Number of words to generate (commonly 12/15/18/21/24). Defaults to 24.
        """

        if words is None:
            self.mnemo = create_new_mnemo(entropy, password, words_count)
        else:
            self.mnemo = PyMnemonic(words, password)

    def get_words(self) -> List[str]:
        """Return mnemonic words as a list of strings."""
        return self.mnemo.get_words()

    def get_private_key_hex(self) -> str:
        """Derive and return the ED25519 private key as a hex string."""
        return self.mnemo.get_private_key_hex()

    def get_private_key(self) -> PrivateKey:
        """Derive and return the ED25519 PrivateKey instance."""
        return PrivateKey(key=self.mnemo.get_private_key())
