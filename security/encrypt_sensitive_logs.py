from ingestion.secure_log_loader import load_secure_logs, split_sensitive_and_safe
from security.field_crypto import encrypt_sensitive_records

DATA_FILE = "data/secure_comm_logs.csv"

def main():
    df = load_secure_logs(DATA_FILE)
    sensitive_df, safe_df = split_sensitive_and_safe(df)

    count = encrypt_sensitive_records(sensitive_df)
    print(f"Encrypted {count} sensitive communication records.")

if __name__ == "__main__":
    main()
