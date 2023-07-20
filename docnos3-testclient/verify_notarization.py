'''
Simple script to test DocNoS API function "verify"

configuration see config.py

@author    Chris Baumann <cba@infinite-trust-digital.com>, <c.baumann@baumann.at>
@version   v0.5 2023/07/20

'''
import sys
import hashlib
import json
import requests  # install with "pip3 install requests" if necessary

from config import *

print('------------------------------------------------')
print('DocNos for - Test ... verify')

# SHA2 256
sha256_hash_to_verify = hashlib.sha256(
    defaultContent.encode('utf-8')).hexdigest()
# print(sha256_hash_to_verify)

httpHeaders = {
    'Accept': 'application/json',
    'X-ApiToken': apiToken
}

# search for specific hash
# prefix required
key = 'hash'
value = 'sha256:' + sha256_hash_to_verify


# OR search for an id (UUID)
# prefix required
#key = 'id'
#value = 'id:12345678-5f7c-4eb2-9344-b35943815ed5'

# OR search by transaction
#key = 'txid'
#value = '8877873041300b8ce01b0429523764e26b34422e9cfa7df532fd464a7ce89b03'


# OR search by blockhash (new in v1.6.x)
'''
key = 'blockHash'
value = '00a72a6c434c46a334c0101698c6124c13b01675f2ade6b1281d00dc1827457b'
'''

response = requests.get(url_verify, params={key: value}, headers=httpHeaders)

print(str(response.headers))

print(str(response))
print('Raw RESULT: ' + response.text)

parsed_res = json.loads(response.text)
beautified_res = json.dumps(parsed_res, indent=2)
print('Beautified RESULT: ')
print(beautified_res)
