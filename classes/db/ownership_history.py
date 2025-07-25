from classes.db.data_structures.sll import sll

class OwnershipHistory:
    def __init__(self):
        self.history = sll()

    def add(self, new_entry):
        return self.history.add_first(new_entry)
    
    def get_writeable(self):
        return self.__repr__()

    def __repr__(self):
        rp = "CarID | OwnerNationalID | StartDate | EndDate | PlateNumber\n"
        rp += self.history.__repr__()
        return rp
        