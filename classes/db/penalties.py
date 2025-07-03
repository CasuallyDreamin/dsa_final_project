from db.data_structures.hashtable import hashtable
from classes.penalty import Penalty

class Penalties:
    def __init__(self):
        self.penalties = hashtable()

    def add(self, id, penalty: Penalty)->bool:
        self.penalties.insert(id, penalty)

    def get(self, id)->Penalty:
        return self.penalties.get(id)
    
    def get_all(self):
        return self.penalties.get_all()
