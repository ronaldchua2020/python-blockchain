# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:41:27 2020

@author: magicolas
"""
import time
import sys
sys.path.append('C:/Users/ronal/Anaconda3/envs/blockchain-env/Lib/site-packages')
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
sys.path.append('C:/Users/ronal/python-blockchain/backend/blockchain')
sys.path.append('C:/Users/ronal/python-blockchain/backend/blockchain/wallet')
from block import Block
from transaction import Transaction   
pnconfig= PNConfiguration()
pnconfig.subscribe_key= 'sub-c-a0baf7a4-68e0-11ea-95b7-3ec3e5ef3302'
pnconfig.publish_key= 'pub-c-3a48ced5-671c-4c2d-a65c-bd0562663fe8'




CHANNELS= {
        'TEST': 'TEST',
         'BLOCK': 'BLOCK',
         'TRANSACTION':'TRANSACTION'
        
        
}

class Listener(SubscribeCallback):
    
    def __init__(self,blockchain, transaction_pool):
        self.blockchain= blockchain
        self.transaction_pool= transaction_pool
    def message(self, pubnub, message_object):
        print(f'\n--Channel: {message_object.channel} | Message: {message_object.message}')
        
        if message_object.channel == CHANNELS['BLOCK']:
            block=Block.from_json(message_object.message)
            potential_chain= self.blockchain.chain[:]
            potential_chain.append(block)
            
            try:            
                self.blockchain.replace_chain(potential_chain)
                self.transaction_pool.clear_blockchain_transactions(
                        self.blockchain
                        
                )
                print('\n-- Successfully replaced the local chain')
                
            except Exception as e:
                print(f'\n -- Did not replace chain: {e}')
                
        elif message_object.channel == CHANNELS['TRANSACTION']:
            transaction= Transaction.from_json(message_object.message)
            self.transaction_pool.set_transactioon(transaction)
            print('n -- Set the new transaction in the transaction pool')
            
            


class PubSub():
    """
    Handles the publish/subscribe layer of the application
    Provides communication between the nodes of the blockchain network.
    """
    def __init__(self, blockchain, transaction_pool):
        self.pubnub= PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain, transaction_pool))
        
        
    def publish(self,channel,message):
        """
        Publish the message object to the channel.
        """
        self.pubnub.publish().channel(channel).message(message).sync()
        
    def broadcast_block(self,block):
        """
        Broadcast a block object to all nodes.
        """
        self.publish(CHANNELS['BLOCK'],block.to_json())
        
    
    def broadcast_transaction(self,transaction):
        """
        Broadcast a transaction to all nodes.
        """
        self.publish(CHANNELS['TRANSACTION'], transaction.to_json())
    


def main():
    pubsub= PubSub()    
    time.sleep(1)
    pubsub.publish(CHANNELS['TEST'],{'foo': 'bar'})
    

if __name__=='__main__':
    main()