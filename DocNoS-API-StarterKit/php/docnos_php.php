<?php
/**
 * DocNoS "StarterKit" in PHP
 *
 * Test functions for DocNoS API.
 *
 * Author: Chris Baumann <c.baumann@baumann.at>
 * Version: v0.7.0 2025/03/10
 */

// Configuration
$URL_CREATE = 'https://blockchains.web-lab.at/docnos3-api/create/';
$URL_VERIFY = 'https://blockchains.web-lab.at/docnos3-api/verify/';
$API_TOKEN = 'starterKit/test/44ede16fa685b3be6b874a01a21f8fff4c6f613a4f3f6b169179fe59956bb914'; // Replace with your actual API token
$DEFAULT_CONTENT = 'This is just some content, which is used as input example ... 123abcxyz php';

function create_notarization() {
    global $URL_CREATE, $API_TOKEN, $DEFAULT_CONTENT;

    echo "------------------------------------------------\n";
    echo "DocNos - Test ... create\n";

    // Hash input data
    $sha256_hash = hash('sha256', $DEFAULT_CONTENT);
    $sha512_hash = hash('sha512', $DEFAULT_CONTENT);

    // Optional UUID for document ID
    $uuid = '12345678-5f7c-4eb2-9344-b35943815ed5';

    // Prepare request data
    $hashes = ['sha256' => $sha256_hash, 'sha512' => $sha512_hash];
    $request = ['id' => $uuid, 'hashes' => $hashes, 'remarks' => 'sent from starterKit (PHP) 0.7.0'];

    // Convert request to JSON
    $post_data = json_encode($request);
    echo "JSON-Request:\n";
    echo $post_data . "\n";
    echo "------------------------------------\n";

    // Prepare HTTP headers
    $http_headers = [
        'Content-type' => 'application/json',
        'Accept' => 'application/json',
        'Content-Length' => strlen($post_data),
        'X-ApiToken' => $API_TOKEN,
    ];
    print_r($http_headers);

    // Send POST request
    $options = [
        'http' => [
            'header'  => implode("\r\n", array_map(function($key, $value) { return "$key: $value"; }, array_keys($http_headers), $http_headers)),
            'method'  => 'POST',
            'content' => $post_data,
            'ignore_errors' => true,
        ],
    ];
    $context  = stream_context_create($options);
    $response = file_get_contents($URL_CREATE, false, $context);
    $response_headers = $http_response_header;

    echo implode("\n", $response_headers) . "\n";
    echo "RESULT: " . $response . "\n";
}

function verify_notarization() {
    global $URL_VERIFY, $API_TOKEN, $DEFAULT_CONTENT;

    echo "------------------------------------------------\n";
    echo "DocNos for - Test ... verify\n";

    // Calculate SHA256 hash for verification
    $sha256_hash_to_verify = hash('sha256', $DEFAULT_CONTENT);

    // Prepare HTTP headers
    $http_headers = ['Accept' => 'application/json', 'X-ApiToken' => $API_TOKEN];

    // Search for specific hash (prefix required)
    $key = 'hash';
    $value = 'sha256:' . $sha256_hash_to_verify;

    // Example: Search for an ID (UUID)
    // $key = 'id';
    // $value = 'id:12345678-5f7c-4eb2-9344-b35943815ed5';

    // Example: Search by transaction ID
    // $key = 'txid';
    // $value = '8877873041300b8ce01b0429523764e26b34422e9cfa7df532fd464a7ce89b03';

    // Example: Search by block hash (new in v1.6.x)
    // $key = 'blockHash';
    // $value = '00a72a6c434c46a334c0101698c6124c13b01675f2ade6b1281d00dc1827457b';

    // Send GET request
    $query = http_build_query([$key => $value]);
    $options = [
        'http' => [
            'header' => implode("\r\n", array_map(function($key, $value) { return "$key: $value"; }, array_keys($http_headers), $http_headers)),
            'method' => 'GET',
            'ignore_errors' => true,
        ],
    ];
    $context = stream_context_create($options);
    $response = file_get_contents($URL_VERIFY . '?' . $query, false, $context);
    $response_headers = $http_response_header;

    echo implode("\n", $response_headers) . "\n";
    echo "Raw RESULT: " . $response . "\n";

    // Beautify JSON response
    $parsed_response = json_decode($response, true);
    $beautified_response = json_encode($parsed_response, JSON_PRETTY_PRINT);
    echo "Beautified RESULT: \n";
    echo $beautified_response . "\n";
}

// Execute test functions
create_notarization();
verify_notarization();
?>