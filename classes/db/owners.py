from db.data_structures.hashtable import hashtable

class Owners:
    def __init__(self):
        self.owners = hashtable()

    def add_owner(self, owner):
        self.owners.insert(owner.nid, owner)
        return True

    def get_owner(self, nid):
        return self.owners.get(nid)

    def get_all_owners(self):
        return self.owners.get_all()