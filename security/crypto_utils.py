from cryptography.fernet import Fernet
import hashlib
from pathlib import Path

KEY_FILE = "security/secret.key"


def generate_key():
    """
    Generate and store a symmetric encryption key.
    """
    key = Fernet.generate_key()
    Path("security").mkdir(exist_ok=True)

    with open(KEY_FILE, "wb") as f:
        f.write(key)

    return key


def load_key():
    """
    Load encryption key from disk.
    """
    if not Path(KEY_FILE).exists():
        return generate_key()

    with open(KEY_FILE, "rb") as f:
        return f.read()


def encrypt_data(data: bytes) -> bytes:
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(data)


def decrypt_data(token: bytes) -> bytes:
    key = load_key()
    fernet = Fernet(key)
    return fernet.decrypt(token)


def compute_hash(data: bytes) -> str:
    """
    Compute SHA-256 hash for integrity verification.
    """
    return hashlib.sha256(data).hexdigest()
