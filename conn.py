from web3 import Web3
import json
w3=Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
try:
    if w3.isConnected():
        print('connected!')
except:
    print('non connected!')
with open('abi.json','r') as f:
    abi=json.load(f)
vote_contract=w3.eth.contract(address='0xAf2aAf9361F963aB44679BE804Ccd2Eb6416d520',#subtitute the address with your own deployment result
                              abi=abi)

if __name__=='__main__':
    pass

