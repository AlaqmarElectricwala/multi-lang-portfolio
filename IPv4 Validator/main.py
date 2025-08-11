import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Match four groups of 1-3 digits separated by dots, no leading zeros unless single digit
    pattern = r"^([1-9]\d{0,2}|0)\.([1-9]\d{0,2}|0)\.([1-9]\d{0,2}|0)\.([1-9]\d{0,2}|0)$"
    match = re.fullmatch(pattern, ip)
    if not match:
        return False
    # Check each octet is in 0-255 and no leading zeros
    for octet in match.groups():
        if not 0 <= int(octet) <= 255:
            return False
        if len(octet) > 1 and octet.startswith("0"):
            return False
    return True

if __name__ == "__main__":
    main()
