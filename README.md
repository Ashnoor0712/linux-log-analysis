# Linux Log-Based Intrusion Analysis

## Scenario
Simulated unauthorized login attempts in a Linux environment and analyzed authentication logs to detect suspicious activity.

## Data Source
System logs from:
- `/var/log/auth.log`

## Tools Used
- Linux (Ubuntu)
- Python
- Terminal commands (`grep`, `cat`)

## Sample Log Evidence
Example entries:
```text
Failed password for invalid user admin from 192.168.1.10 port 22 ssh2
Failed password for root from 192.168.1.10 port 22 ssh2

## Analysis
- Detected repeated failed login attempts from a single IP address: 192.168.1.10
- Observed multiple login attempts targeting different usernames
- Activity pattern suggests a potential brute-force attempt against SSH access

## Automation
- A Python script (log_monitor.py) was used to:
- Parse authentication logs
- Count failed login attempts by IP address
- Flag suspicious activity based on repeated failures

## Output
Example script output:
Suspicious IPs:
192.168.1.10 → 3 failed attempts

## Conclusion
The log activity indicates a likely brute-force attempt targeting SSH authentication. Repeated failed login attempts from a single IP suggest malicious or unauthorized access behavior.
