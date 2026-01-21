from cryptography.fernet import Fernet
import json
from pathlib import Path

KEY_PATH = "security/defense.key"
ENCRYPTED_OUTPUT = "secure_storage/encrypted_sensitive_logs.bin"


def load_or_create_key():
    Path("security").mkdir(exist_ok=True)

    if not Path(KEY_PATH).exists():
        key = Fernet.generate_key()
        with open(KEY_PATH, "wb") as f:
            f.write(key)
    else:
        with open(KEY_PATH, "rb") as f:
            key = f.read()

    return Fernet(key)


def encrypt_sensitive_records(df):
    """
    Encrypt sensitive fields row-wise and store securely.
    """
    fernet = load_or_create_key()
    Path("secure_storage").mkdir(exist_ok=True)

    encrypted_records = []

    for _, row in df.iterrows():
        payload = {
            "timestamp": str(row["timestamp"]),
            "source_node": row["source_node"],
            "destination_node": row["destination_node"],
            "channel_type": row["channel_type"]
        }

        encrypted = fernet.encrypt(json.dumps(payload).encode())
        encrypted_records.append(encrypted)

    with open(ENCRYPTED_OUTPUT, "wb") as f:
        for record in encrypted_records:
            f.write(record + b"\n")

    return len(encrypted_records)
