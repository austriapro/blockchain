<?php
/********************************************************************************
AUSTRIAPRO Blockchain Lab - Demo

Write data to Blockchain (Multichain) stream

5/2022
C. Baumann - AUSTRIAPRO
********************************************************************************/

require_once('config.php');
require_once('multichain-api.php');

// initialize RPC connection to Multichain Instance
$chain = new MultiChain($cfg->rpcUser, $cfg->rpcPass, $cfg->rpcHost, $cfg->rpcPort, $cfg->rpcPath, $cfg->timeout);

// check for initialization errors (e.g. curl not available)
if (!$chain->initOK) {
	echo("##### ERROR\r\n");
	echo($chain->error);
	exit();
}

// check for RPC connection errors
$info = $chain->getinfo();
if (!$info) {
	echo("##### ERROR\r\n");
	echo($chain->error);
	exit();
}

/*
build data structure in JSON format, e.g.
{
    "timeStamp": "2021-05-09T11:46:00+02:00",
    "client": "AustriaPro Lab Client 2",
    "data": {
        "name": "some Name",
        "value": 14,
        "hash": "sha256:8527a891e224136950ff32ca212b45bc93f69fbb801c3b1ebedac52775f99e61",
        "remark": "some remark for value 14"
    }
}
*/

class cData{};
$data = new cData();
$timeStamp = date('c');
$data->timeStamp = $timeStamp;
$data->client = $cfg->client;

$clientData = new cData();
$clientData->name = 'some Name';
$value = rand(0, 100);
$clientData->value = $value;
$clientData->hash = 'sha256:' . hash('sha256', $value);
$clientData->remark = 'some remark for value ' . $value;

$data->data = $clientData;

// prepare to publish in JSON mode
$dataToPublish = array('json' => $data);

// show data to be published
var_dump($dataToPublish);

// prepare stream keys
$keys = array();
$keys[] = $cfg->key;
$keys[] = 'another key';

// publish data and keys to configured multichain stream
$res = $chain->publish($cfg->stream, $keys, $dataToPublish);

// check & show result
if ($res == false) {
	echo("##### ERROR publishing data\r\n");
	echo($chain->error);
	exit();
} else {
	echo("##### publishing data OK\r\n");
	echo("transaction-Id: $res\r\n");
}

?>