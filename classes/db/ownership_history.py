from classes.ownership_entry import OwnershipEntry
from classes.db.data_structures.sll import sll
from classes.car import Car

class OwnershipHistory:
    def __init__(self):
        self.history = sll()

    def add(self, new_entry):
        return self.history.add_first(new_entry)
    
    def __repr__(self):
        rp = "CarID | OwnerNationalID | StartDate | EndDate | PlateNumber\n"
        rp += self.history.__repr__()
        return rp
        