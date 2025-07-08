from classes.history_entry import History_entry
from classes.db.data_structures.sll import sll
from classes.car import Car

class Ownership_history:
    def __init__(self):
        self.history = sll()

    def add(self, new_car: Car, date):
        
        new_entry = History_entry(new_car.id,
                                  new_car.owner_nid,
                                  date)
        
        self.history.add_first(new_entry)

    def __repr__(self):
        rp = "CarID | OwnerNationalID | Date\n"
        rp += self.history.__repr__()
        return rp
        