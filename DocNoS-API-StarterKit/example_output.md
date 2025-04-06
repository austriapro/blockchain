
# Example output

(Java)
------------------------------------------------
DocNos - Test ... create
JSON-Request:

{"hashes":{"sha256":"bbdca52ab6a9d4e6fde17b145e54f436e2875086b955d278645bbd6ec7c47a07","sha512":"fa3bdf94ff03dd7df52a327240750524f963575374705bef7dfc2bc9d89a63b1b52a15a0591ced67006382c30e47669a0a2988e5be2f38689b8dc7f91a8376e3"},"id":"12345678-5f7c-4eb2-9344-b35943815ed5","remarks":"sent from starterKit (Java) 0.7.0"}

sun.net.www.protocol.https.DelegateHttpsURLConnection:https://blockchains.web-lab.at/docnos3-api/create/
Response Code : 200

RESULT: {"success":"OK, data published in transaction 60a1458ed06499a29a7bc72a47103d733ded8c979bc0a219a21b3fd1b7b9ea11","timeStamp":"2025-04-06T15:35:05+02:00","id":"12345678-5f7c-4eb2-9344-b35943815ed5","txid":"60a1458ed06499a29a7bc72a47103d733ded8c979bc0a219a21b3fd1b7b9ea11","service":"DocNoS receiver\/create v1.6.2","infos":"client:starterKit v:1 stream:docnos-test-1 chain:mc2b1 rpc:127.0.0.1:7222"}

------------------------------------------------
DocNos for - Test ... verify

{Keep-Alive=[timeout=5, max=99], null=[HTTP/1.1 200 OK], Server=[Apache/2.4.18], Access-Control-Allow-Origin=[*], Connection=[Keep-Alive], Content-Length=[835], Access-Control-Allow-Headers=[content-type, x-apitoken], Date=[Sun, 06 Apr 2025 13:35:05 GMT], Content-Type=[application/json]}
sun.net.www.protocol.https.DelegateHttpsURLConnection:https://blockchains.web-lab.at/docnos3-api/verify/?hash=sha256:bbdca52ab6a9d4e6fde17b145e54f436e2875086b955d278645bbd6ec7c47a07

Raw RESULT: 
{"success":"hash found: sha256:bbdca52ab6a9d4e6fde17b145e54f436e2875086b955d278645bbd6ec7c47a07","data":[{"publisher":"13VXwdarLRtV5fyP8qdWEFXebe6Ay45pgdY4Bb","txid":"60a1458ed06499a29a7bc72a47103d733ded8c979bc0a219a21b3fd1b7b9ea11","blockHash":null,"blockTime":null,"confirmations":0,"data":{"timeStamp":"2025-04-06T15:35:05+02:00","client":"starterKit","version":"DocNoS-v1.1","data":{"id":"12345678-5f7c-4eb2-9344-b35943815ed5","hashes":{"sha256":"bbdca52ab6a9d4e6fde17b145e54f436e2875086b955d278645bbd6ec7c47a07","sha512":"fa3bdf94ff03dd7df52a327240750524f963575374705bef7dfc2bc9d89a63b1b52a15a0591ced67006382c30e47669a0a2988e5be2f38689b8dc7f91a8376e3"},"remarks":"sent from starterKit (Java) 0.7.0"}}}],"service":"DocNoS receiver\/verify v1.6.2","infos":"client:starterKit v:1 stream:docnos-test-1 chain:mc2b1 rpc:127.0.0.1:7222"}

Beautified RESULT: 

    {
      "data": [{
        "blockHash": null,
        "data": {
          "timeStamp": "2025-04-06T15:35:05+02:00",
          "data": {
            "hashes": {
              "sha256": "bbdca52ab6a9d4e6fde17b145e54f436e2875086b955d278645bbd6ec7c47a07",
              "sha512": "fa3bdf94ff03dd7df52a327240750524f963575374705bef7dfc2bc9d89a63b1b52a15a0591ced67006382c30e47669a0a2988e5be2f38689b8dc7f91a8376e3"
            },
            "id": "12345678-5f7c-4eb2-9344-b35943815ed5",
            "remarks": "sent from starterKit (Java) 0.7.0"
          },
          "client": "starterKit",
          "version": "DocNoS-v1.1"
        },
        "publisher": "13VXwdarLRtV5fyP8qdWEFXebe6Ay45pgdY4Bb",
        "txid": "60a1458ed06499a29a7bc72a47103d733ded8c979bc0a219a21b3fd1b7b9ea11",
        "blockTime": null,
        "confirmations": 0
      }],
      "success": "hash found: sha256:bbdca52ab6a9d4e6fde17b145e54f436e2875086b955d278645bbd6ec7c47a07",
      "service": "DocNoS receiver/verify v1.6.2",
      "infos": "client:starterKit v:1 stream:docnos-test-1 chain:mc2b1 rpc:127.0.0.1:7222"
    }
Note, that the blockHash, blockTime and confirmations are not set, if verifyNotarization() is called immediately after createNotarization(). This is, because the Blocktime is e.g. 15 seconds and the data will be set, when the next block is created.

Calling verifyNotatization() after some time shows a result like e.g.

     {
          "data": [{
            "blockHash": "00424baffb1237c0942103dee6bd4b59225d3d8ab8bc473e3dcbf7126a8ef09d",
            "data": {
              "timeStamp": "2025-04-06T15:35:05+02:00",
              "data": {
                "hashes": {
                  "sha256": "bbdca52ab6a9d4e6fde17b145e54f436e2875086b955d278645bbd6ec7c47a07",
                  "sha512": "fa3bdf94ff03dd7df52a327240750524f963575374705bef7dfc2bc9d89a63b1b52a15a0591ced67006382c30e47669a0a2988e5be2f38689b8dc7f91a8376e3"
                },
                "id": "12345678-5f7c-4eb2-9344-b35943815ed5",
                "remarks": "sent from starterKit (Java) 0.7.0"
              },
              "client": "starterKit",
              "version": "DocNoS-v1.1"
            },
            "publisher": "13VXwdarLRtV5fyP8qdWEFXebe6Ay45pgdY4Bb",
            "txid": "60a1458ed06499a29a7bc72a47103d733ded8c979bc0a219a21b3fd1b7b9ea11",
            "blockTime": "2025-04-06T15:35:21+02:00",
            "confirmations": 21
          }],
          "success": "hash found: sha256:bbdca52ab6a9d4e6fde17b145e54f436e2875086b955d278645bbd6ec7c47a07",
          "service": "DocNoS receiver/verify v1.6.2",
          "infos": "client:starterKit v:1 stream:docnos-test-1 chain:mc2b1 rpc:127.0.0.1:7222"
        }

Note the difference between timeStamp (of the transaction) and the blockTime of some seconds.
