# block.py
# implementation of a class for a single block in the blockchain
# NOTE: The structure of this code is partially borrowed from https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/

from hashlib import sha256
import json

class Block:

    def __init__(self, index, timestamp, transactions, previous_hash, proof=0):

        # private instance variables
        self._index = index
        self._timestamp = timestamp
        self._transactions = transactions
        self._previous_hash = previous_hash
        self._proof = proof

    # compute hash value of this block
    def compute_hash(self):

        # get json string containing info in this block (sort keys to make sure
        # this is repeatable)
        block_info = json.dumps(self.__dict__, sort_keys=True)
        
        # get and return hash of this string using sha256 function (put it into hex form)
        res = sha256(block_info.encode()).hexdigest()
        return res

    # getters and setters
    def get_index(self):
        return self._index
    
    def get_timestamp(self):
        return self._timestamp
    
    def get_transactions(self):
        return self._transactions

    def get_previous_hash(self):
        return self._previous_hash

    def get_proof(self):
        return self._proof

    def set_proof(self, proof):
        self._proof = proof
    
    # NOT SURE IF NEED THIS, WILL SEE HOW THE DESIGN BUILDS OUT
    def set_transactions(self, transactions):
        self._transactions = transactions