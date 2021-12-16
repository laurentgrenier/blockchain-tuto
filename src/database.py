import hashlib
import json


class FieldUpdateBlock:

    def __init__(self, previous_hash, actor , update):
        self.previous_hash = previous_hash
        self.update = update

        self.data = {'actor': actor, 'previous_hash': previous_hash, 'update': update}

        # maybe we could specify the encoding to ensure an uniform encoding through the platforms
        self.hash = hashlib.sha256(json.dumps(self.data).encode()).hexdigest()


class FieldUpdateBlockChain:
    NO_ONE = ''

    def __init__(self):
        self.chain = []
        self.generate_base_block()

    def generate_base_block(self):
        self.chain.append(FieldUpdateBlock('0', self.NO_ONE, ['empty']))

    def apply_update(self, actor, update):
        previous_hash = self.last_update.hash
        self.chain.append(FieldUpdateBlock(previous_hash, actor, update))

    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {json.dumps(self.chain[i].data)}")
            print(f"Hash {i + 1}: {self.chain[i].hash}\n")

    def check(self):
        for i in range(1, len(self.chain)):
            if self.has_unique_ancestor(i):
                print(f"{i} OK")
            else:
                print(f"{i} KO")

    @property
    def last_update(self):
        return self.chain[-1]

    def has_unique_ancestor(self, i):
        return len([1 for block in self.chain if block.hash == self.chain[i].data['previous_hash']]) == 1



t1 = "George sends 3.1 GC to Joe"
t2 = "Joe sends 2.5 GC to Adam"
t3 = "Adam sends 1.2 GC to Bob"
t4 = "Bob sends 0.5 GC to Charlie"
t5 = "Charlie sends 0.2 GC to David"
t6 = "David sends 0.1 GC to Eric"

field_chain = FieldUpdateBlockChain()

field_chain.apply_update('laurent', ['empty', 'value 1'])
field_chain.apply_update('roger', ['value 1', 'value 2'])
field_chain.apply_update('henry', ['value 2', 'value 3'])

field_chain.display_chain()
field_chain.check()

print(" insert hacked value")
field_chain.chain.append(FieldUpdateBlock('1aa82f70377ed9cbf48fb766fab78d5e1cd76dce69930cf14c1b6fc5bfa7e004', 'hacker', ['value 1', 'value 10']))
field_chain.display_chain()
field_chain.check()
