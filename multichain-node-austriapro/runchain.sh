#!/bin/bash -x

echo "Setup multichain.conf"

mkdir -p /root/.multichain/apro-lab-1/

cat << EOF > /root/.multichain/apro-lab-1/multichain.conf
rpcuser=multichainrpc
rpcpassword=5F1qcAXD6DZS1TfJ2PmZDAhEdFHFS8Vh857sXPF1MBm7
rpcallowip=0.0.0.0/0.0.0.0
rpcport=7176
autosubscribe=assets,streams
#Note: do not edit directly, file will be overwritten by runchain.sh next time docker starts
EOF

echo "Start the chain: apro-lab-1"
multichaind apro-lab-1@88.99.145.156:7177
