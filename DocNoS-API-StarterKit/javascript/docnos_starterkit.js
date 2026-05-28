// DocNoS "StarterKit" in JavaScript
// Test functions for DocNoS API.
// Author: Chris Baumann <c.baumann@baumann.at>
// Version: v0.8.0 2026/05/26

/*
How to run:
1) npm install axios
2) node docnos_starterkit.js
*/

const crypto = require('crypto');
const axios = require('axios'); 

// Configuration
const URL_CREATE = 'https://blockchains.web-lab.at/docnos3-api/create/';
const URL_VERIFY = 'https://blockchains.web-lab.at/docnos3-api/verify/';
const API_TOKEN = 'starterKit/test/44ede16fa685b3be6b874a01a21f8fff4c6f613a4f3f6b169179fe59956bb914'; // Replace with your actual API token

const DEFAULT_CONTENT = 'This is just some content, which is used as input example ... 123abcxyz 123456 javascript NotarizeIfNew Test!';

function createNotarization() {
    console.log('------------------------------------------------');
    console.log('DocNos - Test ... create');

    // Hash input data
    const sha256Hash = crypto.createHash('sha256').update(DEFAULT_CONTENT, 'utf8').digest('hex');
    const sha512Hash = crypto.createHash('sha512').update(DEFAULT_CONTENT, 'utf8').digest('hex');

    // Optional UUID for document ID
    const uuid = '12345678-5f7c-4eb2-9344-b35943815e07';

    // Prepare request data
    const hashes = { sha256: sha256Hash, sha512: sha512Hash };
    const request = {
        id: uuid,
        hashes: hashes,
        notarizeIfNew: true,
        remarks: 'sent from starterKit (JavaScript) 0.8.0'
    };

    const postData = JSON.stringify(request);

    console.log('JSON-Request:');
    console.log(postData);
    console.log('------------------------------------');

    // Prepare HTTP headers
    const headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-ApiToken': API_TOKEN
    };

    console.log('Headers:');
    console.log(headers);

    // Send POST request
    axios.post(URL_CREATE, postData, { headers })
        .then(response => {
            console.log(`RESULT: ${response.data}`);
        })
        .catch(err => {
            console.error('Error during POST:', err.response?.data || err.message);
        });
}

function verifyNotarization() {
    console.log('------------------------------------------------');
    console.log('DocNos - Test ... verify');

    // Calculate SHA256 hash for verification
    const sha256HashToVerify = crypto.createHash('sha256').update(DEFAULT_CONTENT, 'utf8').digest('hex');

    // Prepare HTTP headers
    const headers = {
        'Accept': 'application/json',
        'X-ApiToken': API_TOKEN
    };

    // Search for specific hash (prefix required)
    const key = 'hash';
    const value = `sha256:${sha256HashToVerify}`;

    // Example: Search by ID
    // const key = 'id';
    // const value = 'id:12345678-5f7c-4eb2-9344-b35943815e07';

    // Example: Search by transaction ID
    // const key = 'txid';
    // const value = '8877873041300b8ce01b0429523764e26b34422e9cfa7df532fd464a7ce89b03';

    // Example: Search by block hash (new in v1.6.x)
    // const key = 'blockHash';
    // const value = '00a72a6c434c46a334c0101698c6124c13b01675f2ade6b1281d00dc1827457b';

    // Send GET request
    const url = `${URL_VERIFY}?${key}=${encodeURIComponent(value)}`;

    axios.get(url, { headers })
        .then(response => {
            console.log(`Raw RESULT: ${response.data}`);
            try {
                const beautified = JSON.stringify(response.data, null, 2);
                console.log('Beautified RESULT:');
                console.log(beautified);
            } catch (e) {
                console.error('Failed to parse JSON:', e);
            }
        })
        .catch(err => {
            console.error('Error during GET:', err.response?.data || err.message);
        });
}

// Execute test functions
createNotarization();
verifyNotarization();