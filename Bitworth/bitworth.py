import sys
import requests as r

# Check no.of Command Line Arguments
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument ")

# Check For Valid Command Line Argument
try:
    n = float(sys.argv[1])
except:
    sys.exit("Command-line argument is not a number ")

# Get response from API in json format an store it in content
try:
    response = r.get(
        "https://rest.coincap.io/v3/assets?apiKey=132a813acefa6610d163409b60bcaf3811a3f9ba163057c05f98d5c46788d0ca"
    )
    response.raise_for_status()
except r.RequestException:
    sys.exit("Invalid Request")
content = response.json()

# Get price of bitcoin
try:
    price = float(content['data']['priceUsd'])
except (KeyError, TypeError, ValueError):
    sys.exit()

# Print total price of bitcoin
print(f"${price*n:,.4f}")
