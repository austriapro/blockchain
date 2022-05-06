'''
DatNos API test client

@copyright 2021/2022 baumann.at
@author    Chris Baumann <c.baumann@baumann.at>
@version   v0.4 2022/05/06

A valid DatNos request looks like this: 
{
   "keys":[
      "auto-capture-123",
      "VIE"
   ],
   "data":{
      "device":"33123b9d-5f7c-4eb2-9344-b35943815ed5",
      "temp":12.34190,
      "hum":56.731,
      "power":0.4231,
      "timeStamp":"2022-05-06T09:33:12.093486",
      "comment":"n/a"
   }
}
'''

import sys
from datetime import datetime
import hashlib
import json
import random
import requests # install with "pip3 install requests" if necessary

apiUrl = 'https://blockchains.web-lab.at/datnos-api/'
# following apiToken is not valid
# get your apiToken from c.baumann@baumann.at
apiToken = 'c235b4ff1d7a9ca8a8a7fa8740512bbfb6a8f13b'

print('------------------------------------')
print('DatNos Test ...')

# example for document id, device id ...
uuid = '33123b9d-5f7c-4eb2-9344-b35943815ed5'

# current date/time
timeStamp = datetime.now().isoformat()

# set up some data
temp = random.uniform(-10, 30)
hum = random.uniform(0, 100)
power = random.uniform(0.1, 2.2)

# example data
data = {
    "timeStamp": timeStamp,
    'device': uuid,
    'temp': temp,
    'hum': hum,
    'power': power,
    'comment': 'n/a'
}

# example for keys
keys = ["auto-capture-123", "VIE"] 

# example request 
request = {
    'keys': keys,
    'data': data
}

postData = json.dumps(request)
print('JSON-Request:')
print(postData)
print('------------------------------------')

length = str(len(postData))

httpHeaders = {
    'Content-type':'application/json',
    'Accept':'application/json',
    'Content-Length': length,
    'X-ApiToken': apiToken}

print('HTTP Headers:')
print(httpHeaders)
print('------------------------------------')


response = requests.post(apiUrl, data = postData, headers = httpHeaders)
print(str(response))
print('RESULT: ' + response.text) 
