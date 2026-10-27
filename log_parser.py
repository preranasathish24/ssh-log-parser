import re
import sys
from collections import Counter

# This pattern finds failed SSH logins and captures the username and the IP address.
# Group 1 = "invalid user " (o`r nothing), group 2 = username, group 3 = IP address.
FAILED_PATTERN = re.compile(
    r"Failed password for (invalid user )?(\S+) from (\d+\.\d+\.\d+\.\d+)"
)

# An IP with this many failures or more gets flagged as suspicious.
THRESHOLD = 3


def parse_log(path):
    """Return a list of (username, ip) for every failed login in the file."""
    failures = []

    # TODO 1 completed
    with open(path, "r") as file:
        for line in file:
            match = FAILED_PATTERN.search(line)
            if match:
                username = match.group(2)
                ip = match.group(3)
                failures.append((username, ip))

    return failures


def count_by_ip(failures):
    """Return a Counter of how many failures each IP address has."""

    # TODO 2 completed
    return Counter(ip for user, ip in failures)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 log_parser.py <logfile>")
        sys.exit(1)

    failures = parse_log(sys.argv[1])
    counts = count_by_ip(failures)

    print(f"Total failed logins: {len(failures)}")
    print("IPs over the threshold:")

    # TODO 3 completed
    for ip, count in counts.most_common():
        if count >= THRESHOLD:
            print(f"{ip}: {count}")


if __name__ == "__main__":
    main()