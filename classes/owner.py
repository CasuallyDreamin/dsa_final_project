from classes.user import User
from classes.db.cars import Cars

class Owner:
    def __init__(self, nid):
        self.nid = nid
        self.cars = Cars()
    
    def get_cars(self):
        return self.cars