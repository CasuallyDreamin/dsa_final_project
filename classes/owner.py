from classes.user import User
from classes.db.cars import Cars

class owner(User):
    def __init__(self, nid, name, family_name, birth_date, password):
        super().__init__(nid, name, family_name, birth_date, password)
        self.cars = Cars()
    
    def get_cars(self):
        return self.cars