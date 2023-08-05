#!/bin/bash -x

echo "Setup multichain.conf"
mkdir -p /root/.multichain/apro-lab-2/
cat << EOF > /root/.multichain/apro-lab-2/multichain.conf
rpcuser=multichainrpc
#Change to other some password  
rpcpassword=5F1rcAXD6DZS1TgJ2PmZDAhEdFHFS8Vh857sXPF1MBm3
rpcallowip=0.0.0.0/0.0.0.0
rpcport=7770
autosubscribe=assets,streams
#Note: do not edit directly, file will be overwritten by runchain.sh next time docker starts
EOF

echo "Start the chain: apro-lab-2"
multichaind apro-lab-2@88.99.145.156:7771
