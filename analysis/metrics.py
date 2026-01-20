import pandas as pd

LATENCY_THRESHOLD_MS = 1000
PACKET_SIZE_THRESHOLD = 4000

def compute_metrics(df: pd.DataFrame) -> dict:
    metrics = {}

    metrics["total_events"] = len(df)
    metrics["avg_response_time_ms"] = df["response_time_ms"].mean()
    metrics["max_response_time_ms"] = df["response_time_ms"].max()

    metrics["high_latency_events"] = df[df["response_time_ms"] > LATENCY_THRESHOLD_MS].shape[0]
    metrics["large_packet_events"] = df[df["packet_size"] > PACKET_SIZE_THRESHOLD].shape[0]

    metrics["failure_events"] = df[df["status"] == "FAIL"].shape[0]

    return metrics


def detect_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["high_latency_flag"] = df["response_time_ms"] > LATENCY_THRESHOLD_MS
    df["large_packet_flag"] = df["packet_size"] > PACKET_SIZE_THRESHOLD
    df["failure_flag"] = df["status"] == "FAIL"

    df["anomaly"] = (
        df["high_latency_flag"] |
        df["large_packet_flag"] |
        df["failure_flag"]
    )

    return df
