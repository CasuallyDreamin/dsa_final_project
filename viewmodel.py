from db import DataBase
from datetime import date

class ViewModel:
    def __init__(self, Database: DataBase):
        self.curr_user = None
        self.sys_date = date.today()
        self.db: DataBase = Database

    # NOTE: All implementation of validation, login check
    # or any other logic beside manipulating data must be done here.
    # DB only does the CRUD operations. 

    def add_user(self, new_user):
        return self.db.add_user(new_user)
    
    def add_plate(self, new_plate):
        return self.db.add_plate(new_plate)    

    def plate_car(self, new_car, plate_date):
        return self.db.add_car(new_car, plate_date)

    def get_user(self, nid):
        return self.db.get_user(nid)

    def get_car(self, car_id):
        return self.db.get_car(car_id)

    def get_all_cars(self):
        return self.db.get_all_cars()

    def get_all_users(self):
        return self.db.get_all_users()

    def get_all_plates(self):
        return self.db.get_all_plates()
        
    def get_plates_from(self, city):
        return self.db.get_plates_from(city)

    def get_cars_from(self, city):
        return self.db.get_cars_from(city)

    def get_owners_from(self, city):
        return self.db.get_owners_in(city)
    
    def get_cars_between(self, first_year, last_year):
        return self.db.get_cars_between(first_year, last_year)
    
    def get_owners_in(self, city):
        return self.db.get_owners_in(city)
    
    def change_user_name(self, nid, new_name, new_family_name):
        return self.db.change_user_name(nid, new_name, new_family_name)
    
    def login(self, national_id, password):
        user = self.db.get_user(national_id)
        
        if not user or user.password != password:
            return False
        
        self.curr_user = user
        return True
    