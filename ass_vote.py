from web3 import Web3
import json
import sys

def Ass_vote(addr): #addr means the address of smart contract
    w3=Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545")) 
    with open('abi.json','r') as f:
        abi=json.load(f)
    vote_contract=w3.eth.contract(address=addr,abi=abi)
    
    #here I just set number of voters and amount assigned to each voter both equal 5
    num_voters=5
    amount_per_voter=5
    #here i use the first address >>w3.eth.accounts[0]<< as the contract constructor 
    
    print('Start assigning votes...')
    for i in range(1,num_voters+1):
        vote_contract.functions.Give_right_to_voters(w3.eth.accounts[i],amount_per_voter).transact(transaction={'from':w3.eth.accounts[0]})
    print('Assigned Done!')
    return w3,vote_contract
