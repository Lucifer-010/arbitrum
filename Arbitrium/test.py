123b94b1cd8d4664be0b8c2334766d16

from web3 import Web3

# Replace with your Infura/Alchemy endpoint
infura_url = "https://sepolia.infura.io/v3/123b94b1cd8d4664be0b8c2334766d16"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())  # Check if connected to Sepolia
