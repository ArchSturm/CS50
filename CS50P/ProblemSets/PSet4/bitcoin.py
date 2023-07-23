import json
import sys
import requests

try:
    n = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
     sys.exit("Command-line argument is not a number")
while True:
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        break
    except requests.RequestException:
        pass
    
o = r.json()

rate = o["bpi"]["USD"]["rate_float"]

s = rate * n

print(f"${s:,.4f}")