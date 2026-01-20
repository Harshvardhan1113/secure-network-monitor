import pandas as pd

REQUIRED_COLUMNS = [
    "timestamp",
    "source_ip",
    "destination_ip",
    "protocol",
    "packet_size",
    "response_time_ms",
    "status"
]

def load_csv_logs(file_path: str) -> pd.DataFrame:
    """
    Load and validate CSV-based network/event logs.
    """
    df = pd.read_csv(file_path)

    missing_cols = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df["packet_size"] = pd.to_numeric(df["packet_size"], errors="coerce")
    df["response_time_ms"] = pd.to_numeric(df["response_time_ms"], errors="coerce")

    df.dropna(inplace=True)

    return df
