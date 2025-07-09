from db import DataBase
from datetime import date
from classes.user import User

class ViewModel:
    def __init__(self, Database: DataBase):
        self.curr_user: User = None
        self.sys_date = date.today()
        self.db: DataBase = Database

    # NOTE: All implementation of validation, login check
    # or any other logic beside manipulating data must be done here.
    # DB only does the CRUD operations. 
    
    def add_car(self, new_car):
        return self.db.add_car(new_car)
    
    def add_user(self, new_user):
        return self.db.add_user(new_user)
    
    def add_plate(self, new_plate):
        self.curr_user.add_plate(new_plate)
        return self.db.add_plate(new_plate)    

    def plate_car(self, new_car, plate_date):
        self.db.ownership_history.add(new_car, plate_date)
        return self.db.add_car(new_car)
    
    def get_city_code(self, city):
        return self.db.citycode.convert_city_to_code(city)
        
    def get_user(self, nid):
        return self.db.get_user(nid)

    def get_car(self, car_id):
        return self.db.get_car(car_id)
    
    def get_plate(self, plate_number):
        return self.db.get_plate(plate_number)
    
    def get_driver(self, nid):
        return self.db.get_driver(nid)
    
    def get_all_cars(self):
        return self.db.get_all_cars()

    def get_all_users(self):
        return self.db.get_all_users()

    def get_all_plates(self):
        return self.db.get_all_plates()
    
    def get_all_owners(self):
        return self.db.get_all_owners()

    def get_plates_from(self, city):
        return self.db.get_plates_from(city)

    def get_cars_from(self, city):
        return self.db.get_cars_from(city)

    def get_owners_from(self, city):
        return self.db.get_owners_in(city)
    
    def get_cars_between(self, first_year, last_year):
        if last_year == '': last_year = first_year
        
        return self.db.get_cars_between(first_year, last_year)
    
    def get_owners_in(self, city):
        return self.db.get_owners_in(city)

    def get_user_negative_score(self, nid = None):
        if not nid: nid = self.curr_user.nid
        
        user = self.get_user(nid)
        driver = self.get_driver(nid)
        
        if not driver: return f"{user.name} {user.family_name} is not a driver."

        return f"negative score: {driver.score}"

    def get_user_record(self, nid = None):
        if not nid: nid = self.curr_user.nid
        
        user = self.get_user(nid)
        driver = self.get_driver(nid)

        if not driver: return f"{user.name} {user.family_name} is not a driver."             
        
        return driver.get_all_penalties()
    
    def get_plate_record(self, plate):
        plate = self.db.get_plate(plate)
        return plate.get_all_penalties()

    def get_plate_ownership_history(self, plate):
        plate = self.db.get_plate(plate)
        return plate.get_all_history()
    
    def change_user_name(self, nid, new_name, new_family_name):
        return self.db.change_user_name(nid, new_name, new_family_name)
    
    def login(self, national_id, password):
        l_user = self.db.users.get(national_id)
        
        if not l_user:
            input("user not found.")
            return False
        
        elif l_user.password != password:
            input("wrong password.")
            return False

        self.curr_user = l_user
        return True