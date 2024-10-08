# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:12:11 2020

@author: magicolas
"""
import random
import os

import sys
sys.path.append('C:/Users/ronal/Anaconda3/Lib/site-packages')
import requests
from flask import Flask,jsonify, request
sys.path.append('C:/Users/ronal/python-blockchain/backend/blockchain')
sys.path.append('C:/Users/ronal/python-blockchain/backend')
sys.path.append('C:/Users/ronal/python-blockchain/backend/wallet')
from blockchain import Blockchain
from wallet import Wallet
from transaction import Transaction
from transaction_pool import TransactionPool
from pubsub import PubSub



app= Flask(__name__)
blockchain= Blockchain()
wallet= Wallet()
transaction_pool= TransactionPool()
pubsub= PubSub(blockchain, transaction_pool)
@app.route('/')

def default():
    return 'Welcome to the blockchain'


@app.route('/blockchain')

def route_blockchain():
    return jsonify(blockchain.to_json())

@app.route('/blockchain/mine')
def route_blockchain_mine():   
    
    transaction_data= transaction_pool.transaction_data()
    transaction_data.append(Transaction.reward_transaction(wallet).to_json())
    blockchain.add_block(transaction_data)
    block=blockchain.chain[-1]
    pubsub.broadcast_block(block)
    transaction_pool.clear_blockchain_transactions(blockchain)
    return jsonify(block.to_json())

@app.route('/wallet/transact', methods= ['POST'])

def route_wallet_transact():
    
    transaction_data = request.get_json()
    transaction = transaction_pool.existing_transaction(wallet.address)
    
    if transaction:
        transaction.update(
                wallet,
                transaction_data['recipient'],
                transaction_data['amount']
                
        )
        
    else:
        transaction= Transaction(
                wallet,
                transaction_data['recipient'],
                transaction_data['amount']
                
                
        )
    
    Transaction(
            wallet,
            transaction_data['recipient'],
            transaction_data['amount']
    )
    
    print (f'transaction.to_json(): {transaction.to_json()}')    
    pubsub.broadcast_transaction(transaction)
    
    
    return jsonify(transaction.to_json())
    
  

ROOT_PORT= 5000
PORT = ROOT_PORT

if os.environ.get('PEER') == 'True':
    PORT= random.randint(5001,6000)
    result= requests.get(f'http://localhost:{ROOT_PORT}/blockchain')
    print(f'result.json(): {result.json()}')
    
    result_blockchain= Blockchain.from_json(result.json())
    try:
        blockchain.replace_chain(result_blockchain.chain)
        print('\n -- Successfully synchronized the local chain')
    except Exception as e:
        print (f'\n -- Error synchronizing: {e}')       
    
        
                                        
           
app.run(port=PORT)
