# blockchain.py
# implementation of a class for the entire blockchain
# NOTE: The structure of this code is partially borrowed from https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/

import time
from blockchain.block import *

class Blockchain:

    def __init__(self):
        
        # initialize empty chain and pending transactions as private variables
        self._chain = []
        # maybe implement as a deque
        self._pending_transactions = []

        # difficulty variable for computing proof of work
        self._difficulty = 2

        # create initial block
        self.create_initial_block()
    
    # initialize the first block in the chain
    def create_initial_block(self):

        # create block object for this initial block
        initial_block = Block(0, time(), [], "0")
        
        # get this block's hash value
        initial_block.hash = initial_block.compute_hash()
        
        # add this block to the chain
        self.chain.append(initial_block)

    # method to compute proof of work variable for a single block
    def proof_of_work(self, block):

        # get the hash of this block
        hash = block.compute_hash()

        # re-compute hash with new proof until we get a hash that starts with
        # "difficulty" number of zeroes
        while not hash.startswith('0' * self._difficulty):

            # increment the proof, recompute hash
            block.set_proof(block.get_proof() + 1)
            hash = block.compute_hash()
        
        # set the value of the proof to this final computed hash
        block.set_proof(hash)

    # add a new block to the chain
    def add_block(self, block, proof):

        # get previous hash of the last block in the chain
        previous_hash = self.last_block.hash

        # make sure this hash matches the previous_hash variable in the new block
        if not previous_hash == block.get_previous_hash():
            return False

        # MORE HERE    

    # return the last block in the chain
    def get_last_block(self):
        return self._chain[-1]

    