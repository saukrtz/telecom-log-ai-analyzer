import os

def generate_logs():
    log_content = """2026-05-08 10:00:01 INFO Starting Kafka consumer...
2026-05-08 10:05:23 ERROR Kafka consumer lag exceeded threshold
2026-05-08 10:05:24 INFO Retrying connection to broker-1...
2026-05-08 10:05:45 ERROR Connection timeout at broker-2
2026-05-08 10:06:10 WARN Rebalancing consumer group 'telecom-monitoring-group'
2026-05-08 10:06:15 INFO Consumer group rebalanced successfully.
"""
    log_file = "app.log"
    with open(log_file, "w") as f:
        f.write(log_content)
    print(f"Log file {log_file} created successfully.")

if __name__ == "__main__":
    generate_logs()
