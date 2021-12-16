import hashlib

"""
class GeekCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        # maybe we could specify the encoding to ensure an uniform encoding through the platforms
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
"""

import json


class GeekCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = {'transactions': transaction_list, 'previous_block_hash': previous_block_hash}
        # maybe we could specify the encoding to ensure an uniform encoding through the platforms
        self.block_hash = hashlib.sha256(json.dumps(self.block_data).encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(GeekCoinBlock("0", ['Genesis Block']))

    def create_block_from_transaction(self, transaction_list):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(GeekCoinBlock(previous_block_hash, transaction_list))

    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {json.dumps(self.chain[i].block_data)}")
            print(f"Hash {i + 1}: {self.chain[i].block_hash}\n")

#    def check(self):
#        for i in range(1,len(self.chain)):
#            if (self.chain[i].block_data.split(' - '))
    @property
    def last_block(self):
        return self.chain[-1]


"""
t1 = "Joakim sends 13 GC to Derrick"
t2 = "Derrick sends 1 GC to Demar"
t3 = "Demar sends 11 GC to Lonzo"
t4 = "Lonzo sends 2 GC to Zac"

# step 1
b1 = GeekCoinBlock('001', [t1,t2])
print(f"Block 1 data: {b1.block_data}")
print(f"Block 1 hash: {b1.block_hash}")

# step 2
b2 = GeekCoinBlock(b1.block_hash, [t3,t4])
print(f"Block 1 data: {b2.block_data}")
print(f"Block 1 hash: {b2.block_hash}")
"""

t1 = "George sends 3.1 GC to Joe"
t2 = "Joe sends 2.5 GC to Adam"
t3 = "Adam sends 1.2 GC to Bob"
t4 = "Bob sends 0.5 GC to Charlie"
t5 = "Charlie sends 0.2 GC to David"
t6 = "David sends 0.1 GC to Eric"

myblockchain = Blockchain()

myblockchain.create_block_from_transaction([t1, t2])
myblockchain.create_block_from_transaction([t3, t4])
myblockchain.create_block_from_transaction([t5, t6])

myblockchain.display_chain()
