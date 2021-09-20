from solcx import compile_standard, install_solc

install_solc("0.6.0")

with open("./SimpleStorage.sol", "r") as file:
    Simple_Storage_file = file.read()
    # print(Simple_Storage_file)

# Compile our solidity

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
