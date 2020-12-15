#!/usr/bin/python

import requests
import json

url="http://admin.quantumvectorcap.com/gw/sys-mgt/openapi/attribution"

payload = {
  'attributionType': 'alpha',
  'attributionName': '施老师',
  'tradingDay': '20200728',
  'value': 0.2341
}
headers = {'content-type': 'application/json'}
r = requests.post(url, headers=headers, data=json.dumps(payload))

print (r.status_code)
print (r.content)
