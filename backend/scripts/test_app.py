# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:30:46 2020

@author: magicolas
"""

import time
import sys
import requests
sys.path.append('C:/Users/ronal/python-blockchain/backend/wallet')
from wallet import Wallet
BASE_URL= 'http://localhost:5000'

def get_blockchain():
    requests.get(f'{BASE_URL}/blockchain').json()
    
def get_blockchain_mine():
    return requests.get(f'{BASE_URL}/blockchain/mine').json()

def post_wallet_transact(recipient, amount):
    return requests.post(
            f'{BASE_URL}/wallet/transact',
            json={'recipient': recipient, 'amount': amount}
            
    ).json()
    
start_blockchain= get_blockchain()
print(f'start_blockchain: {start_blockchain}')

recipient= Wallet().address
post_wallet_transact_1= post_wallet_transact(recipient,21)
print(f'\npost_wallet_transact_1: {post_wallet_transact_1}')

post_wallet_transact_2= post_wallet_transact(recipient,13)
print(f'\npost_wallet_transact_2: {post_wallet_transact_2}')

time.sleep(1)
mined_block= get_blockchain_mine()
print(f'\nmined_block: {mined_block}')

