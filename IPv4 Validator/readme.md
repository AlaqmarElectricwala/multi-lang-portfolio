# IPv4 Address Validator in Python

A Python program that validates IPv4 addresses using regular expressions and additional numeric checks.  
Includes a comprehensive test suite to verify correctness for valid addresses, invalid ranges, bad formats, and leading zero cases.

## Features
- Validates IPv4 address format (`X.X.X.X`)
- Rejects addresses with leading zeros (e.g., `01.2.3.4`)
- Checks each octet is in range 0–255
- Includes unit tests using `pytest`

## How to Run
```bash
python main.py
