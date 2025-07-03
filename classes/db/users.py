from .data_structures.hashtable import hashtable
from classes.user import User

class Users:
    def __init__(self):
        self.ht = hashtable()
        # TODO: implement data structure for city based get all
        
    def add(self, user: User):
        self.ht.insert(user.nid, user)
        return True

    def get(self, nid: str)->User:
        return self.ht.get(nid)

    def exists(self, nid: str)->bool:
        if self.get_user(nid): return True
        else: return False

    def get_all(self):
        return self.ht.get_all()


    