from classes.user import User
from classes.db.cars import Cars

class Owner:
    def __init__(self, nid):
        self.nid = nid
        self.cars = Cars()
    
    def get_cars(self):
        return self.cars
    
    def add_car(self, new_car):
        self.cars.add(new_car)

    def __repr__(self):
        return f"\nOwner National ID: {self.nid}\ncars:\n{self.cars.get_all()}"