from .data_structures.hashtable import hashtable

class Plates:    
    def __init__(self):
        self.ht = hashtable()

    def add(self, plate):
        self.ht.insert(plate.number, plate)
        return True

    def get(self, number: str):
        return self.ht.get(number)

    def exists(self, number: str):
        if self.get_user(number): return True
        else: return False

    def get_all(self):
        return self.ht.get_all()