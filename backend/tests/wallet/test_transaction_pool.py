# -*- coding: utf-8 -*-
"""
Created on Sat May  9 18:32:12 2020

@author: magicolas
"""
import sys
sys.path.append('C:/Users/ronal/python-blockchain/backend/wallet')
sys.path.append('C:/Users/ronal/python-blockchain/backend/blockchain')
from transaction_pool import TransactionPool
from transaction import Transaction
from wallet import Wallet
from blockchain import Blockchain

def test_set_transaction():
    transaction_pool= TransactionPool()
    transaction= Transaction(Wallet(), 'recipient', 1)
    transaction_pool.set_transaction(transaction)
    
    assert transaction_pool.transaction_map[transaction.id]== transaction

def test_clear_blockchain_transactions():    
    transaction_pool= TransactionPool()
    transaction_1= Transaction(Wallet(), 'recipient', 1)
    transaction_2= Transaction(Wallet(),'recipient',2)
    
    transaction_pool.set_transaction(transaction_1)
    transaction_pool.set_transaction(transaction_2)
    
    blockchain= Blockchain()
    blockchain.add_block([transaction_1.to_json(), transaction_2.to_json()])
    
    assert transaction_1.id in transaction_pool.transaction_map
    assert transaction_2.id in transaction_pool.transaction_map
    
    transaction_pool.clear_blockchain_transactions(blockchain)
    
    assert not transaction_1.id in transaction_pool.transaction_map
    assert not transaction_2.id in transaction_pool.transaction_map
    
    
                          
