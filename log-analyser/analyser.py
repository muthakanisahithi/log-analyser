import re
from collections import Counter

LOG_FILE = "sample.log"
THRESHOLD = 3  # failed attempts before we flag an IP

failed_by_ip = Counter()
failed_by_user = Counter()

with open(LOG_FILE) as f:
    for line in f:
        if "login failed" in line:
            user = re.search(r"user=(\S+)", line)
            ip = re.search(r"ip=(\S+)", line)
            if user and ip:
                failed_by_user[user.group(1)] += 1
                failed_by_ip[ip.group(1)] += 1

print("=== Security Report ===")
print("Total failed logins:", sum(failed_by_ip.values()))

print("\nSuspicious IPs (possible brute force):")
for ip, count in failed_by_ip.items():
    if count >= THRESHOLD:
        print(f"  {ip} -> {count} failed attempts")

print("\nFailed attempts by user:")
for user, count in failed_by_user.most_common():
    print(f"  {user}: {count}")