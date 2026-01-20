import csv
import random
from datetime import datetime, timedelta

OUTPUT_FILE = "sample_logs.csv"
NUM_RECORDS = 5000   # change to 10000 later if needed

PROTOCOLS = ["HTTP", "HTTPS"]
STATUSES = ["OK", "DELAY", "FAIL"]

def random_ip():
    return f"192.168.1.{random.randint(1, 254)}"

start_time = datetime(2025, 1, 1, 10, 0, 0)

with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "timestamp",
        "source_ip",
        "destination_ip",
        "protocol",
        "packet_size",
        "response_time_ms",
        "status"
    ])

    current_time = start_time

    for _ in range(NUM_RECORDS):
        current_time += timedelta(seconds=random.randint(1, 3))

        # Normal traffic
        packet_size = random.randint(100, 1500)
        response_time = random.randint(50, 300)
        status = "OK"

        # Introduce anomalies
        if random.random() < 0.1:  # 10% delayed
            response_time = random.randint(800, 1500)
            status = "DELAY"

        if random.random() < 0.05:  # 5% failures
            packet_size = random.randint(4000, 8000)
            response_time = random.randint(1500, 3000)
            status = "FAIL"

        writer.writerow([
            current_time.strftime("%Y-%m-%d %H:%M:%S"),
            random_ip(),
            random.choice(["8.8.8.8", "8.8.4.4", "1.1.1.1"]),
            random.choice(PROTOCOLS),
            packet_size,
            response_time,
            status
        ])

print(f"Generated {NUM_RECORDS} log records in {OUTPUT_FILE}")
