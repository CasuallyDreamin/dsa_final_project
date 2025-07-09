from classes.db.ownership_history import OwnershipHistory
from classes.car import Car
from classes.penalty import Penalty
from classes.db.penalties import Penalties

class Plate:
    def __init__(self, plate_number, car_id = None, owner_nid = None):
        self.number = plate_number
        self.car_id = car_id
        self.owner_nid = owner_nid
        self.ownership_history = OwnershipHistory()
        self.penalties = Penalties()

    def add_car(self, new_car: Car, plate_date):
        self.car_id = new_car.id
        self.owner_nid = new_car.owner_nid
        return self.ownership_history.add(new_car, plate_date)

    def add_penalty(self, new_penalty: Penalty):
        return self.penalties.add(new_penalty)
    
    def add_ownership_entry(self, new_entry):
        return self.ownership_history.add(new_entry)
    
    def get_all_penalties(self):
        return self.penalties.get_all()
    
    def get_all_history(self):
        return self.ownership_history
    
    def __repr__(self):
        return f"{self.number} | {self.car_id} | {self.owner_nid}"