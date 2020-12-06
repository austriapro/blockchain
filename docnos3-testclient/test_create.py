'''
Simple script to test DocNoS API function "create"

configuration see test_common.py

@copyright 2020 baumann.at
@author    Chris Baumann <c.baumann@baumann.at>
@version   v0.3 2020/12/06

'''
import sys
import datetime
import hashlib
import json
import requests # install with "pip3 install requests" if necessary

from test_common import *

print('------------------------------------')
print('DocNos Test ... create')

'''
A valid DocNos Create Request looks like this: 
- id is an optional (v4) UUID e.g. for a document-id. If not present, it will be generated from the API
- hashes: sha256 is required, sha512 and sha3/512 optional
- remarks: optional, used for testing
{
        "id" : "1c123b9d-5f7c-4eb2-9344-b35943815ef1",
        "hashes": {
            "sha256": "1a482edb60960719895a6b1c50121c938a62357cd68fe9ab29be1b8b343b663c",
            "sha512": "294a725daacea98a340ce946182105e12448e7c1147424f94a0eb453eb531373a39f0e563d828aea092e53d4481a02282ca3ba313a029bf5c09956759de26363",
            "sha3\/512": "f210c7bc0c281b844a989160186eb0f8a1ac2a996cd3d6db8e0b4074815e3521b50dccbd2ac597c7192a692e16f2ffa0491a0823a991212af44c2a8c3087dec0"
        },
        "remarks": "optional remarks"
} 

'''

# Build API request
# SHA2 256
sha256  = hashlib.sha256(defaultContent.encode('utf-8')).hexdigest()
#print(sha256)
# SHA2 512
sha512  = hashlib.sha512(defaultContent.encode('utf-8')).hexdigest()
#print(sha512)
# SHA3 512
sha3_512  = hashlib.sha3_512(defaultContent.encode('utf-8')).hexdigest()
#print(sha3_512)
#print('------------------------------------')

uuid = '1c123b9d-5f7c-4eb2-9344-b35943815ed5'

# example hashes using just the required sha256 hash
'''
hashes = {
  'sha256': sha256
}
'''

#example hashes using more different hashes
hashes = {
  'sha256': sha256,
  'sha512': sha512,
  'sha3/512' : sha3_512  	
}

# example request using the optional UUID
request = {
  'id': uuid,
  'hashes': hashes,
  'remarks': 'sent from pyDemo 0.3'
}

# minimal example of request
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
  'Content-type':'application/json',
	'Accept':'application/json',
	'Content-Length': length,
	'X-ApiToken': apiToken}
#print(httpHeaders)

response = requests.post(url_create, data = postData, headers = httpHeaders)
print(str(response))
print('RESULT: ' + response.text) 
