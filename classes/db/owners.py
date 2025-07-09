from .data_structures.hashtable import hashtable

class Owners:
    def __init__(self):
        self.owners = hashtable()

    def add(self, owner):
        return self.owners.insert(str(owner.nid), owner)
        

    def get(self, nid):
        return self.owners.get(str(nid))

    def get_all(self):
        return self.owners.get_all()