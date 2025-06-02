from .data_structures.hashtable import hashtable


class Users:
    def __init__(self):
        self.ht = hashtable()

    def add(self, user):
        self.ht.insert(user.nid, user)
        return True

    def get(self, nid: str):
        return self.ht.get(nid)

    def exists(self, nid: str):
        if self.get_user(nid): return True
        else: return False

    def get_all(self):
        return self.ht.get_all()


    