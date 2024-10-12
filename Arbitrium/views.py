from django.shortcuts import render

# Create your views here.
from web3 import Web3
import json

 
test_url = "https://sepolia.infura.io/v3/123b94b1cd8d4664be0b8c2334766d16"

contract_address = "0xa3e8a000e21A31BBe00FA84fc45c846cEf0cEF46"

contract_abi = '''
[
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_number",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_aboutMe",
				"type": "string"
			}
		],
		"name": "addUser",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			}
		],
		"name": "getUserInfo",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"name": "userInfos",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "number",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "aboutMe",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
'''



web3 = Web3(Web3.HTTPProvider(test_url))
print(web3.is_connected())

contract = web3.eth.contract(address=contract_address,abi=contract_abi)
data = contract.functions.getUserInfo("melody").call()
print(data)

def getlog(name):
	web3 = Web3(Web3.HTTPProvider(test_url))
	print(web3.is_connected())

	contract = web3.eth.contract(address=contract_address,abi=contract_abi)
	data = contract.functions.getUserInfo("melody").call()
	return data

private_key = "1150fd7ca9a0f1c6dc1a69b719d1610a9efa5df32b7939f4ea4d5f3aea2b8fb9"
wal = "0x0ce3937e3bb15853B18c779bd1b599828baC088D"

# Replace with your account address (where the transaction originates)
account = web3.eth.account.from_key(private_key)

# Build transaction
#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


def home(request):
    return render(request,"home.html",{})


def getinfo(request):
    pass