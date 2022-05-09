<?php

class cConfig{};

//AustriaPro Labs 2 chain "apro-labs-2"
$cfg = new cConfig();
$cfg->rpcHost = '192.168.10.42';
$cfg->rpcPort = 17770; //default: 7770
$cfg->rpcUser = 'multichainrpc';
$cfg->rpcPass = '--- RPC PASSWORD HERE ---';
$cfg->rpcPath = null; // e.g. when using a proxy
$cfg->timeout = 5; // default: 10 [s]

$cfg->stream = 'playground';

$cfg->client = 'AustriaPro Lab Client 2';
$cfg->key = 'AP-key-2';

?>