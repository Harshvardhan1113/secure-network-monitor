from flask import Blueprint, jsonify
from ingestion.secure_log_loader import load_secure_logs, split_sensitive_and_safe
from analysis.system_health import compute_system_health

bp = Blueprint("defense_metrics", __name__)

DATA_FILE = "data/secure_comm_logs.csv"

@bp.route("/api/system/health")
def system_health():
    df = load_secure_logs(DATA_FILE)
    _, safe_df = split_sensitive_and_safe(df)

    anomaly_count = safe_df[
        (safe_df["latency_ms"] > 1500) | (safe_df["status"] == "FAIL")
    ].shape[0]

    return jsonify(compute_system_health(safe_df, anomaly_count))


@bp.route("/api/system/distribution")
def system_distribution():
    df = load_secure_logs(DATA_FILE)
    _, safe_df = split_sensitive_and_safe(df)

    total = len(safe_df)

    return jsonify({
        "status": {
            "SUCCESS": round((safe_df[safe_df["status"] == "SUCCESS"].shape[0] / total) * 100, 2),
            "DELAY": round((safe_df[safe_df["status"] == "DELAY"].shape[0] / total) * 100, 2),
            "FAIL": round((safe_df[safe_df["status"] == "FAIL"].shape[0] / total) * 100, 2),
        },
        "latency_bands": {
            "NORMAL": int((safe_df["latency_ms"] < 300).sum()),
            "ELEVATED": int(((safe_df["latency_ms"] >= 300) & (safe_df["latency_ms"] < 800)).sum()),
            "DEGRADED": int(((safe_df["latency_ms"] >= 800) & (safe_df["latency_ms"] < 1500)).sum()),
            "CRITICAL": int((safe_df["latency_ms"] >= 1500).sum())
        }
    })
