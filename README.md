# Linux Log-Based Intrusion Analysis

##  Scenario
Simulated unauthorized login attempts in a Linux environment and analyzed authentication logs to detect suspicious activity.

##  Data Source
System logs from:
- /var/log/auth.log

##  Tools Used
- Linux (Ubuntu)
- Python (for log parsing)
- Terminal commands (grep, cat)

## Sample Log Evidence
Example entries:
Failed password for invalid user admin from 192.168.1.10 port 22 ssh2
Failed password for root from 192.168.1.10 port 22 ssh2

##  Analysis
- Detected repeated failed login attempts from a single IP (192.168.1.10)
- Pattern indicates potential brute-force attack
- Multiple invalid usernames attempted

##  Automation
A Python script was used to:
- Parse log files
- Count failed login attempts per IP
- Identify suspicious activity

##  Output
Suspicious IPs:
192.168.1.10 → 3 failed attempts

##  Conclusion
The activity indicates a likely brute-force attempt targeting SSH access.
Repeated failed login attempts from a single IP suggest malicious intent.

##  Recommendations
- Disable password-based SSH login
- Enable key-based authentication
- Implement fail2ban or similar protection
