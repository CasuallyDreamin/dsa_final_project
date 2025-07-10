from .data_structures.hashtable import hashtable
from classes.plate import Plate

class Plates:    
    def __init__(self):
        self.ht = hashtable()

    def add(self, plate: Plate):
        return self.ht.insert(str(plate.number), plate)
        
    def get(self, number: str)-> Plate:
        return self.ht.get(str(number))

    def exists(self, number: str):
        if self.get(number): return True
        else: return False

    def get_all(self):
        return self.ht.get_all()
    
    def get_writeable(self):
        return self.__repr__()
