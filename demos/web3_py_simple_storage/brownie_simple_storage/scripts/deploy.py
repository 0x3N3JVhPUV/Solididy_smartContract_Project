from brownie import SimpleStorage, accounts, config, network


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from":account})
    print("simple_storage : ",simple_storage)
    stored_value = simple_storage.retrieve()
    print("stored_value : ",stored_value)

    transaction = simple_storage.store(15, {"from":account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print("updated_stored_value : ",updated_stored_value)

def get_account():
    if (network.show_active() == "developement"):
        account = accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])            


def main():
    deploy_simple_storage()
