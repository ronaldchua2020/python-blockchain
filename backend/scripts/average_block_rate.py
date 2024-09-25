# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:11:42 2020

@author: magicolas
"""
import time
import sys
sys.path.append('C:/Users/ronal/python-blockchain/backend/blockchain')
from blockchain import Blockchain

sys.path.append('C:/Users/ronal/python-blockchain/backend')
from  config import SECONDS

blockchain= Blockchain()

times= []

for i in range(1000):
    start_time = time.time_ns()
    blockchain.add_block(i)
    
    end_time= time.time_ns()
    time_to_mine= (end_time - start_time) / SECONDS
    times.append(time_to_mine)
    
    average_time = sum(times)/ len(times)
    
    print(f'New block difficulty: {blockchain.chain[-1].difficulty}')
    print(f'Time to mine new block:{time_to_mine}s')
    print(f'Average time to add blocks: {average_time}s\n')
    
    