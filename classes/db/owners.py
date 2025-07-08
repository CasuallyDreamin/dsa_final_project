from .data_structures.hashtable import hashtable

class Owners:
    def __init__(self):
        self.owners = hashtable()

    def add(self, owner):
        self.owners.insert(str(owner.nid), owner)
        return True

    def get(self, nid):
        return self.owners.get(str(nid))

    def get_all(self):
        return self.owners.get_all()