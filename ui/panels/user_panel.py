from classes.user import User
from datetime import datetime
from ..tools.generators import generate_plate
from viewmodel import ViewModel
from classes.plate import Plate

class UserPanel:
    def __init__(self, vm: ViewModel):
        self.curr_user: User = vm.curr_user
        self.vm: ViewModel = vm
    
    def register(self,
                national_id,
                name,
                family_name,
                birth_date: str,
                password):
        
        national_id = int(national_id)

        birth_date = birth_date.split("-")
        birth_date = datetime(int(birth_date[0]),
                              int(birth_date[1]),
                              int(birth_date[2])).date()
        
        new_user = User(
                national_id,
                name,
                family_name,
                birth_date,
                password
        )
        
        return self.vm.add_user(new_user)

    def login(self, national_id, password):
        self.curr_user = self.vm.curr_user
        return self.vm.login(national_id, password)
    
    def create_plate(self, city):
        if not self.vm.curr_user:
            return input("Must be logged in.")
        
        citycode = self.vm.get_city_code(city)

        if citycode:
            new_plate = Plate(plate_number = generate_plate(citycode),
                              owner_nid = self.vm.curr_user.nid)
            self.vm.add_plate(new_plate)
            return new_plate

    def get_user_cars(self):
        if not self.vm.curr_user:
            return input("Must be logged in.")
        
        cars = self.vm.curr_user.cars.get_all()
        return cars

    def get_user_plates(self):
        if not self.vm.curr_user:
            return input("Must be logged in.")
        
        plates = self.vm.curr_user.plates.get_all()
        return plates