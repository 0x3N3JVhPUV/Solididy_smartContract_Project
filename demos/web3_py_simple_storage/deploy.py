from solcx import compile_standard, install_solc

with open("./SimpleStorage.sol", "r") as file:
    Simple_Storage_file = file.read()

# Compile our solidity
install_solc("0.6.0")

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "source": {"SimpleStorage.sol": {"content": Simple_Storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)

print(compiled_sol)
