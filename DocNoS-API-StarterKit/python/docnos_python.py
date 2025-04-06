"""
DocNoS "StarterKit" in Python

Test functions for DocNoS API.

Author: Chris Baumann <c.baumann@baumann.at>
Version: v0.7.0 2025/03/10
"""

import hashlib
import json
import requests
import sys

# Configuration
URL_CREATE = 'https://blockchains.web-lab.at/docnos3-api/create/'
URL_VERIFY = 'https://blockchains.web-lab.at/docnos3-api/verify/'
API_TOKEN = 'starterKit/test/44ede16fa685b3be6b874a01a21f8fff4c6f613a4f3f6b169179fe59956bb914'  # Replace with your actual API token
DEFAULT_CONTENT = 'This is just some content, which is used as input example ... 123abcxyz'


def create_notarization():
    """
    Creates a notarization using the DocNoS API.
    """
    print('------------------------------------------------')
    print('DocNos - Test ... create')

    # Hash input data
    sha256_hash = hashlib.sha256(DEFAULT_CONTENT.encode('utf-8')).hexdigest()
    sha512_hash = hashlib.sha512(DEFAULT_CONTENT.encode('utf-8')).hexdigest()

    # Optional UUID for document ID
    uuid = '12345678-5f7c-4eb2-9344-b35943815ed5'

    # Prepare request data
    hashes = {'sha256': sha256_hash, 'sha512': sha512_hash}
    request = {'id': uuid, 'hashes': hashes, 'remarks': 'sent from starterKit (Python) 0.7.0'}

    # Convert request to JSON
    post_data = json.dumps(request)
    print('JSON-Request:')
    print(post_data)
    print('------------------------------------')

    # Prepare HTTP headers
    http_headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json',
        'Content-Length': str(len(post_data)),
        'X-ApiToken': API_TOKEN,
    }
    print(http_headers)

    # Send POST request
    response = requests.post(URL_CREATE, data=post_data, headers=http_headers)
    print(f'{response}')
    print(f'RESULT: {response.text}')


def verify_notarization():
    """
    Verifies a notarization using the DocNoS API.
    """
    print('------------------------------------------------')
    print('DocNos for - Test ... verify')

    # Calculate SHA256 hash for verification
    sha256_hash_to_verify = hashlib.sha256(DEFAULT_CONTENT.encode('utf-8')).hexdigest()

    # Prepare HTTP headers
    http_headers = {'Accept': 'application/json', 'X-ApiToken': API_TOKEN}

    # Search for specific hash (prefix required)
    key = 'hash'
    value = f'sha256:{sha256_hash_to_verify}'

    # Example: Search for an ID (UUID)
    # key = 'id'
    # value = 'id:12345678-5f7c-4eb2-9344-b35943815ed5'

    # Example: Search by transaction ID
    # key = 'txid'
    # value = '8877873041300b8ce01b0429523764e26b34422e9cfa7df532fd464a7ce89b03'

    # Example: Search by block hash (new in v1.6.x)
    # key = 'blockHash'
    # value = '00a72a6c434c46a334c0101698c6124c13b01675f2ade6b1281d00dc1827457b'

    # Send GET request
    response = requests.get(URL_VERIFY, params={key: value}, headers=http_headers)

    print(f'{response.headers}')
    print(f'{response}')
    print(f'Raw RESULT: {response.text}')

    # Beautify JSON response
    parsed_response = json.loads(response.text)
    beautified_response = json.dumps(parsed_response, indent=2)
    print('Beautified RESULT: ')
    print(beautified_response)


# Execute test functions
create_notarization()
verify_notarization()