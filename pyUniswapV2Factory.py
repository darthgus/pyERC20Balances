from web3 import Web3
import json

# Create a Web3 instance connected to our RPC
w3 = Web3(Web3.HTTPProvider("https://testnet-v925-fireblocks.testnet.z7a.xyz"))

with open("IUniswapV2Factory.json", "r") as fp:
  erc20_abi = json.loads(fp.read())

print([function["name"] for function in erc20_abi if "name" in function])

# XSGD
ERC20_CA = "0xd0156eFCA4D847E4c4aD3F9ECa7FA697bb105cC0"
# USDC
#ERC20_CA = "0x1fD09F6701a1852132A649fe9D07F2A3b991eCfA"

ERC20_CONTRACT = w3.eth.contract(ERC20_CA, abi=erc20_abi)
print(dir(ERC20_CONTRACT.functions))
feeTo = ERC20_CONTRACT.functions.feeTo().call()
print(feeTo)
