import re

log_file = "auth.log"
THRESHOLD = 3

failed_pattern = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")
invalid_user_pattern = re.compile(r"Invalid user .* from (\d+\.\d+\.\d+\.\d+)")

failed_attempts = {}

with open(log_file, "r") as file:
    for line in file:
        match_failed = failed_pattern.search(line)
        match_invalid = invalid_user_pattern.search(line)

        if match_failed:
            ip = match_failed.group(1)
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

        elif match_invalid:
            ip = match_invalid.group(1)
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

print("Suspicious IPs:")
for ip, count in failed_attempts.items():
    if count >= THRESHOLD:
        print(f"{ip} → {count} failed attempts")

print("\nAll Failed Attempts:")
for ip, count in failed_attempts.items():
    print(f"{ip} → {count}")

with open("alerts.txt", "w") as alert_file:
    for ip, count in failed_attempts.items():
        if count >= THRESHOLD:
            alert_file.write(f"{ip} → {count} failed attempts\n")
