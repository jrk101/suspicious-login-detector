# Suspicious Login Detector 

A simple Python tool to scan system logs and detect IP addresses with multiple failed login attempts — simulating a basic Security Operations Center (SOC) task.

## What it does
- Parses log files line by line
- Extracts IP addresses from lines with "Failed login"
- Counts failed login attempts
- Flags IPs with 3 or more failed attempts

##  How to run
Make sure you have Python installed, then:

```bash
python flag_ip.py
