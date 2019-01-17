<?php
/*
Simple demo to get info about assets of an address

C. Baumann 2019/1
*/
require_once('http_lib-0bs.php');

define('ADDRESS', '3Mthq2HwiU4V2AqUmCsT9BV6UTB9MUV5eU9');

$url = 'http://blockchains.web-lab.at:7431/assets/balance/' . ADDRESS;
$res = callUrl($url, true);
var_dump($res);

?>