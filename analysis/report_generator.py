import json
from ingestion.csv_loader import load_csv_logs
from analysis.metrics import compute_metrics, detect_anomalies
from security.crypto_utils import encrypt_data, compute_hash
from pathlib import Path


def generate_secure_report():
    df = load_csv_logs("data/sample_logs.csv")

    metrics = compute_metrics(df)
    anomalies = detect_anomalies(df)
    anomaly_count = anomalies["anomaly"].sum()

    report = {
        "metrics": metrics,
        "total_anomalies": int(anomaly_count)
    }

    report_bytes = json.dumps(report, indent=2).encode("utf-8")

    encrypted_report = encrypt_data(report_bytes)
    report_hash = compute_hash(encrypted_report)

    Path("reports").mkdir(exist_ok=True)

    with open("reports/encrypted_report.bin", "wb") as f:
        f.write(encrypted_report)

    with open("reports/report_hash.txt", "w") as f:
        f.write(report_hash)

    print("Secure report generated successfully.")


if __name__ == "__main__":
    generate_secure_report()
