<?php

/*
calls an url
returns
*) false, if error
*) response as decoded json, if possible or
*) raw response
*/

function callUrl($url, $apiKey, $postData = false, $debug=true) {
	$curl = curl_init($url);
	curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-type: application/json', 'Accept: application/json', "X-API-Key: $apiKey")); 
	curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1); 
	curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, 0); 
	
	if ($postData) {
		curl_setopt($curl, CURLOPT_POST, 1);
		curl_setopt($curl, CURLOPT_POSTFIELDS, $postData);
	}
	
	$raw_response = curl_exec($curl);
	$response = json_decode($raw_response, true); 
	$status = curl_getinfo($curl, CURLINFO_HTTP_CODE);
	$error = curl_error($curl);
	curl_close($curl);
	
	if ($debug) {
		echo("================\r\n");
		echo("called url: $url\r\n");
		echo("status: $status\r\n");
		echo("error: $error\r\n");
		echo("raw response: \r\n$raw_response\r\n");
//		echo("response: \r\n$response\r\n");
	}
	
	if ($error) return false;
	if ($response) return $response;
	return($raw_response);
}

?>