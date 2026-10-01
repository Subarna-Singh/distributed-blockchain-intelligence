#!/bin/bash

# Get the latest block number from Ethereum RPC
# curl -X POST "$ETH_RPC_URL" \
#   -H "Content-Type: application/json" \
#   --data '{
#     "jsonrpc": "2.0",
#     "method": "eth_blockNumber",
#     "params": [],
#     "id": 1
#   }'

# Get Block by Number
curl -X POST "$ETH_RPC_URL" \
  -H "Content-Type: application/json" \
  --data '{
    "jsonrpc": "2.0",
    "method": "eth_getBlockByNumber",
    "params": ["latest", true],
    "id": 1
  }'