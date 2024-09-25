# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 18:30:26 2020

@author: magicolas
"""

import sys
sys.path.append('C:/Users/ronal/python-blockchain/backend/util')
from hex_to_binary import hex_to_binary

def test_hex_to_binary():
    original_number= 789
    hex_number= hex(original_number)[2:]
    binary_number= hex_to_binary(hex_number)
    
    assert int(binary_number,2) == original_number