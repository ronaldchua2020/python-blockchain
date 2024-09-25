# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:43:31 2020

@author: magicolas
"""

import sys
sys.path.append('backend/util')
from crypto_hash import crypto_hash

def test_crypto_hash():
    assert crypto_hash(1, [2], 'three') == crypto_hash('three',1,[2])
    assert crypto_hash('foo') == 'b2213295d564916f89a6a42455567c87c3f480fcd7a1c15e220f17d7169a790b'
    
