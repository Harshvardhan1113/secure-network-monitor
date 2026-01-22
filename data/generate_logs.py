import csv
import random
from datetime import datetime, timedelta

OUTPUT_FILE = "secure_comm_logs.csv"
NUM_RECORDS = 8000

CHANNELS = ["SATCOM", "RF", "FIBER"]
STATUSES = ["SUCCESS", "DELAY", "FAIL"]

def random_node():
    return f"NODE-{random.randint(1000, 9999)}"

start_time = datetime(2025, 1, 1, 0, 0, 0)
current_time = start_time

with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "timestamp",
        "source_node",
        "destination_node",
        "channel_type",
        "latency_ms",
        "message_size",
        "status"
    ])

    for _ in range(NUM_RECORDS):
        current_time += timedelta(seconds=random.randint(1, 4))

        latency = random.randint(40, 250)
        size = random.randint(200, 1500)
        status = "SUCCESS"

        # Simulated network stress
        if random.random() < 0.12:
            latency = random.randint(800, 1600)
            status = "DELAY"

        # Simulated failure / hostile conditions
        if random.random() < 0.05:
            latency = random.randint(1800, 3200)
            size = random.randint(3000, 7000)
            status = "FAIL"

        writer.writerow([
            current_time.strftime("%Y-%m-%d %H:%M:%S"),
            random_node(),
            random_node(),
            random.choice(CHANNELS),
            latency,
            size,
            status
        ])

print(f"Generated {NUM_RECORDS} secure communication logs.")
