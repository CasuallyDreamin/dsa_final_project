from classes.user import user
from datetime import datetime
from ..tools.generators import generate_plate

class UserPanel:
    def __init__(self, vm):
        self.curr_user = vm.curr_user
        self.vm = vm
    
    def register(self,
                name,
                family_name,
                birth_date: str,
                national_id,
                password):
        
        national_id = int(national_id)

        birth_date = birth_date.split("-")
        birth_date = datetime(int(birth_date[0]),
                              int(birth_date[1]),
                              int(birth_date[2]))
        
        new_user = user(
                name,
                family_name,
                birth_date,
                national_id,
                password
        )
        
        return self.vm.add_user(new_user)

    def login(self, national_id, password):
        national_id = int(national_id)
        
        return self.vm.login(national_id, password)
    
    def create_plate(self):
        new_plate = generate_plate()
        self.vm.add_plate(new_plate)
        return new_plate
    
    def get_all_cars(self):
        all_cars = self.vm.get_all_cars()
        # TODO: format the all_cars object into string and return 

    def get_all_plates(self):
        all_plates = self.vm.get_all_plates()
        # TODO: format the all_plates object into string and return
