import requests
import sys
import json

#handling exceptions
if len(sys.argv) == 1:
    sys.exit('Missing command-line argument')
elif len((sys.argv)) > 2:
    sys.exit('Too many arguments')

#users provided number of bitcoins
try:
    number = float(sys.argv[1])
except ValueError:
    sys.exit('Command-line argument is not a number')

#json request from coindest for information about bitcoin
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

#storing that json file in dictionary
o = response.json()

#there is multiple nested dictionaries
for price in o:
    bpi = o['bpi']
    USD = bpi['USD']
    rate = USD['rate_float']
#OMG we can write ',.4f' ',' and '.4f' jointly after ':'
#p.s. after ':' space is matters, there shuldn't be spaces
print(f'${(float(rate) * float(sys.argv[1])) :,.4f}')

