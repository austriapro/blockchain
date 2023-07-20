'''
Simple script to test DocNoS API function "create"

configuration see config.py

@author    Chris Baumann <cba@infinite-trust-digital.com>, <c.baumann@baumann.at>
@version   v0.5 2023/07/20

'''
import sys
import datetime
import hashlib
import json
import requests  # install with "pip3 install requests" if necessary

from config import *

print('------------------------------------------------')
print('DocNos - Test ... create')

'''
A valid DocNos Create Request looks like this: 
- id is an optional (v4) UUID e.g. for a document-id. If not present, it will be generated from the API
- hashes: sha256 is required, sha512 (and sha3/512) optional
- remarks: optional, used for testing
{
    "id": "12345678-5f7c-4eb2-9344-b35943815ed5",
    "hashes": {
        "sha256": "8daf3a72c2bea121e7f8477141bfad7787192a2e0f82680cbf83f55a070fbdbf",
        "sha512": "439eef199e5da58722f459a8e4088c842015fe0458ce27bf8bc5a3d2cdb2fb65b3a61ec3d750bbd8912edc82ffb325cafe052d20ffad5dea185dab6244f6d351"
    },
    "remarks": "sent from pyDemo 0.5"
}
'''

# hash input data (in this case just the content, defined in config.py)
sha256 = hashlib.sha256(defaultContent.encode('utf-8')).hexdigest()
sha512 = hashlib.sha512(defaultContent.encode('utf-8')).hexdigest()

# or create uuid based on some kind of document id etc.
uuid = '12345678-5f7c-4eb2-9344-b35943815ed5'

hashes = {
  'sha256': sha256,
  'sha512': sha512
}

# example request using the optional uuid
request = {
    'id': uuid,
    'hashes': hashes,
    'remarks': 'sent from pyDemo 0.5'
}

# minimal request would be
'''
request = {
  'hashes': hashes
}
'''

postData = json.dumps(request)
print('JSON-Request:')
print(postData)
print('------------------------------------')

length = str(len(postData))

httpHeaders = {
    'Content-type': 'application/json',
    'Accept': 'application/json',
    'Content-Length': length,
    'X-ApiToken': apiToken}
print(httpHeaders)

response = requests.post(url_create, data=postData, headers=httpHeaders)
print(str(response))
print('RESULT: ' + response.text)
