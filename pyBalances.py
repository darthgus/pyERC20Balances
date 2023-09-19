from web3 import Web3
import json

# Create a Web3 instance connected to our RPC
w3 = Web3(Web3.HTTPProvider("https://testnet-v925-fireblocks.testnet.z7a.xyz"))

with open("erc20.json", "r") as fp:
  erc20_abi = json.loads(fp.read())

print([function["name"] for function in erc20_abi if "name" in function])

# XSGD
ERC20_CA = "0x8895Aa1bEaC254E559A3F91e579CF4a67B70ce02"
# USDC
#ERC20_CA = "0x1fD09F6701a1852132A649fe9D07F2A3b991eCfA"

# my address
#ADDRESS = "0x395a414b0c0a8C067e7dD3210cA991145620C4bC"
# feeTo address
ADDRESS = "0x0B64162E95D64Ee844E7962B313b038b4e6d96d3"

ERC20_CONTRACT = w3.eth.contract(ERC20_CA, abi=erc20_abi)
print(dir(ERC20_CONTRACT.functions))
balance = ERC20_CONTRACT.functions.balanceOf(ADDRESS).call()
decimals = ERC20_CONTRACT.functions.decimals().call()
print(balance)
print(decimals)
print(balance / 10 ** decimals)