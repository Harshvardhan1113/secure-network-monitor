import numpy as np

def compute_system_health(safe_df, anomaly_count: int):
    total = len(safe_df)

    return {
        "total_messages": int(total),
        "avg_latency_ms": round(float(safe_df["latency_ms"].mean()), 2),
        "p95_latency_ms": round(float(np.percentile(safe_df["latency_ms"], 95)), 2),
        "failure_rate": round(
            (safe_df[safe_df["status"] == "FAIL"].shape[0] / total) * 100, 2
        ),
        "anomaly_rate": round(
            (anomaly_count / total) * 100, 2
        )
    }
