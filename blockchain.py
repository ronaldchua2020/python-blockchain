# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:15:03 2020

@author: magicolas
"""

import sys
sys.path.append('backend/blockchain')
from block import Block     

class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions
    """
    
    def __init__(self):
        self.chain= [Block.genesis()]
        
    def add_block(self,data):
        
        self.chain.append(Block.mine_block(self.chain[-1],data))
        
    def __repr__(self):
        return f'Blockchain: {self.chain}'
        
def main():        
        
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')
    
    print(blockchain)
    print(f'blockchain.py__name:_: {__name__}')
    
if __name__ == '__main__':
    main()