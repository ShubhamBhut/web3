from brownie import interface, network
from scripts.helpful_scripts import get_account, config

def get_weth():
    #ABI
    #Address
    account = get_account()
    weth = interface.WethInterface(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": 0.1* 10**18})
    print(f"Received 0.1 wETH")
    return tx

def main():
    get_weth()
