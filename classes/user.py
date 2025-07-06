from .db.cars import Cars
from .db.plates import Plates

class User:
    def __init__(self,
                 nid,
                 name,
                 family_name,
                 birth_date,
                 password):
        
        self.nid         = nid
        self.name        = name
        self.family_name = family_name
        self.birth_date  = birth_date
        self.password    = password
        self.cars        = Cars()
        self.plates      = Plates()
    
    def add_car(self, car):
        self.cars.add(car)

    def add_plate(self, plate):
        self.plates.add(plate)
        
    def __repr__(self):
        return f"{self.nid} | {self.name} | {self.family_name} | {self.birth_date} | {self.password}\n {self.cars.get_all()}"