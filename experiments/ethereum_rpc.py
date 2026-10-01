import json 
import os 
import urllib.request 



def process_request(url, payload):
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(request) as response:
        response_data = json.loads(response.read().decode("utf-8"))

    return response_data


payload = {
    "jsonrpc": "2.0",
    "method": "eth_blockNumber",
    "params": [],
    "id": 1
}
block_number = process_request(os.environ.get("ETH_RPC_URL"), payload)["result"]
# print("Latest Block Number:", block_number)

payload_block = {
    "jsonrpc": "2.0",
    "method": "eth_getBlockByNumber",
    "params": [block_number, True],
    "id": 1
}
block_data = process_request(os.environ.get("ETH_RPC_URL"), payload_block)
# print("Block Data:", block_data["result"].keys())
# print("Transactions in Block:", block_data["result"]["transactions"][0].keys())


payload_block = {
    "jsonrpc": "2.0",
    "method": "eth_getTransactionReceipt",
    "params": [block_data["result"]["transactions"][0]["hash"]],
    "id": 1
}
transaction_receipt = process_request(os.environ.get("ETH_RPC_URL"), payload_block)
print("Transaction Receipt:", transaction_receipt["result"]["logs"][0].keys())

