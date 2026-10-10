# Log Analyser

A Python tool that reads authentication logs and detects
failed login attempts and possible brute-force activity.

## How to run
python analyser.py

## What it does
- Counts failed logins per user and per IP
- Flags IPs with 3 or more failed attempts

## Sample output
Suspicious IPs (possible brute force):
  203.0.113.5 -> 4 failed attempts

## Tools
Python (re, collections)
