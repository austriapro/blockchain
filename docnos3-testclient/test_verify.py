'''
Simple script to test DocNoS API function "verify"

configuration see test_common.py

@copyright 2020 baumann.at
@author    Chris Baumann <c.baumann@baumann.at>
@version   v0.2 2020/09/30

'''
import sys
import hashlib
import json
import requests # install with "pip3 install requests" if necessary

from test_common import *

print('------------------------------------')
print('DocNos Test ... verify')

# SHA2 256
sha256_hash_to_verify = hashlib.sha256(defaultContent.encode('utf-8')).hexdigest()
#print(sha256_hash_to_verify)

httpHeaders = {
	'Accept':'application/json'
}

# search for specific hash
key = 'hash'
value = 'sha256:' + sha256_hash_to_verify

# OR search for given transaction-id
#key = 'txid'
#value = '4307fa407a136936fe8deba3babe541b59e5ebe6f8aa7df00ba7fcc83e6b792b'

response = requests.get(url_verify, params={key: value}, headers = httpHeaders)

print(str(response))
print('RESULT: ' + response.text) 
