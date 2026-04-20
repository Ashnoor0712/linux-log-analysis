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
