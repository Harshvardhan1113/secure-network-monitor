import pandas as pd

# Defense-grade data classification
SENSITIVE_FIELDS = [
    "timestamp",
    "source_node",
    "destination_node",
    "channel_type"
]

SAFE_FIELDS = [
    "latency_ms",
    "message_size",
    "status"
]

ALL_FIELDS = SENSITIVE_FIELDS + SAFE_FIELDS


def load_secure_logs(file_path: str) -> pd.DataFrame:
    """
    Load secure communication logs and validate schema.
    """
    df = pd.read_csv(file_path)

    missing = set(ALL_FIELDS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required fields: {missing}")

    # Type normalization
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df["latency_ms"] = pd.to_numeric(df["latency_ms"], errors="coerce")
    df["message_size"] = pd.to_numeric(df["message_size"], errors="coerce")

    df.dropna(inplace=True)
    return df


def split_sensitive_and_safe(df: pd.DataFrame):
    """
    Split logs into sensitive and analytics-safe components.
    """
    sensitive_df = df[SENSITIVE_FIELDS].copy()
    safe_df = df[SAFE_FIELDS].copy()

    return sensitive_df, safe_df
