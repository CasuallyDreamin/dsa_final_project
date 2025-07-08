from classes.db.ownership_history import Ownership_history
from classes.car import Car
class Plate:
    def __init__(self, plate_number, car_id = None, owner_nid = None):
        self.number = plate_number
        self.car_id = car_id
        self.owner_nid = owner_nid
        self.ownership_history = Ownership_history()

    def add_car(self, new_car: Car, plate_date):
        self.car_id = new_car.id
        self.owner_nid = new_car.owner_nid
        self.ownership_history.add(new_car, plate_date)

    def __repr__(self):
        return f"{self.number} | {self.car_id} | {self.owner_nid}"