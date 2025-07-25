from .data_structures.hashtable import hashtable
from classes.penalty import Penalty

class Penalties:
    def __init__(self):
        self.penalties = hashtable()

    def add(self, penalty: Penalty)->bool:
        return self.penalties.insert(str(penalty.id), penalty)

    def get(self, id)->Penalty:
        return self.penalties.get(id)
    
    def get_all(self):
        return self.penalties.get_all()
    
    def get_writeable(self):
        return self.__repr__()


    def __repr__(self):
        return "PenaltyID | DriverID | PlateNumber | PenaltyDate | PenaltyLevel | Description\n" + str(self.get_all())
    
