from solcx import compile_standard, install_solc

# Install the specific version of Solidity compiler
install_solc('0.8.0')

with open("sig.sol", "r") as file:
    simple_storage_file = file.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {
            "SimpleStorage.sol": {
                "content": simple_storage_file
            }
        },
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["*"],
                }
            }
        }
    },
    solc_version='0.8.0',
)

# Get bytecode and ABI
bytecode = compiled_sol['contracts']['sig.sol']['UserData']['evm']['bytecode']['object']
abi = compiled_sol['contracts']['sig.sol']['UserData']['abi']
