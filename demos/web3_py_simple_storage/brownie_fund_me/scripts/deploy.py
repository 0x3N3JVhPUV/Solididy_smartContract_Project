from brownie import FundMe, MockV3Aggregator, config, network
from scripts.helpful_scripts import get_account, deploy_mocks

def deploy_fund_me():
    account = get_account()
    #pass the pricefeed address to our smart contract

    #If we are in a persistence network like rinkeby, use the assopciate address
    #Otherwise deploy mocks
    print(f"network = ", {network.show_active()})
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account}, 
        publish_source=config["networks"][network.show_active()].get("verify")
    )
    print(f"Contract deployed to {fund_me.address}")

def main():
    deploy_fund_me() 