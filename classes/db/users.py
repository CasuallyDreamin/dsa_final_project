from .data_structures.hashtable import hashtable
from classes.user import User

class Users:
    def __init__(self):
        self.ht = hashtable()
        
    def add(self, user: User):
        return self.ht.insert(str(user.nid), user)
        

    def get(self, nid: str)->User:
        nid = str(nid)
        return self.ht.get(nid)

    def exists(self, nid: str)->bool:
        if self.get_user(nid): return True
        else: return False

    def get_all(self):    
        return self.ht.get_all()

    def get_writeable(self):
        return "NationalID | FirstName | LastName | DateOfBirth | Password\n" + str(self.get_all())


    