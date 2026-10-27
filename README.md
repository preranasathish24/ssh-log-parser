# SSH Failed Login Log Parser

## What the script does
This script checks an SSH authentication log for failed login attempts. It finds the username and IP address for each failed login and then counts how many failed attempts came from each IP address.

If an IP address has 3 or more failed attempts, the script displays it as a potentially suspicious IP address.

## How to run it
Make sure `log_parser.py` and `sample_auth.log` are in the same folder.

Open the terminal in that folder and run:

```
python log_parser.py sample_auth.log
```

The script will show the total number of failed logins and any IP addresses that reached the threshold.

For example:

```
Total failed logins: 12
IPs over the threshold:
203.0.113.5: 5
203.0.113.99: 4
```

## Requirements
Python 3, no extra libraries needed.

## Sample data
The `sample_auth.log` file contains made-up sample data. It was created just for testing the script and does not contain real authentication records.

## Limitation
The script only catches failed login messages that contain `Failed password` and match the pattern used in the code. For example, it would miss failed logins using SSH keys, and it only matches IPv4 addresses, not IPv6 addresses.

Name: Prerana Sathish

Date: 27 October 2026
