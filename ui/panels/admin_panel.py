from classes.car import Car
from classes.driver import Driver
from classes.penalty import Penalty

from datetime import datetime, timedelta
from viewmodel import ViewModel
from ui.tools.generators import generate_eight_digit_id, generate_six_digit_id
from ui.tools.validators import validate_six_digit_id

class AdminPanel:
    def __init__(self, vm):
        self.vm: ViewModel = vm

    def plate_car(self,
                color,
                name,
                manuf_date,
                car_id,
                plate_number,
                plate_date):
        
        if plate_date == "": plate_date = str(self.vm.sys_date)

        plate = self.vm.get_plate(plate_number)
        
        if not plate: 
            input("Plate Does not exist.")
            return False
        
        new_car = Car(
                car_id,
                name,
                manuf_date,
                color,
                plate_number,
                plate.owner_nid)
        
        if not self.vm.add_car(new_car):
            input("Car ID already exists.")
            return False
        
        plate.add_car(new_car, plate_date)
        self.vm.plate_car(new_car, plate_date)
        
        return True
        
    def show_all_cars(self):
        all_cars = self.vm.get_all_cars()

        return str(all_cars)

    def show_all_users(self):
        all_users = self.vm.get_all_users()
        
        return str(all_users)
    
    def show_all_plates(self):
        all_plates = self.vm.get_all_plates()
        return str(all_plates)
    
    def show_all_owners(self):
        all_owners = self.vm.get_all_owners()
        return str(all_owners)
    
    def show_all_drivers(self):
        all_drivers = self.vm.get_all_drivers()
        return str(all_drivers)
    
    def delete_car(self, car_id):
        return self.vm.delete_car(car_id)
    
    def delete_driver(self, nid):
        return self.vm.delete_driver(nid)
    
    def show_plates_in(self, city):
        plates = self.vm.get_plates_from(city) 
        return str(plates)

    def show_cars_in(self, city):
        cars = self.vm.get_cars_from(city)    
        return str(cars)

    def show_cars_between(self, 
                        first_year = None,
                        last_year  = None):
        cars = self.vm.get_cars_between(first_year, last_year)
        return cars

    def show_owners_in(self, city):
        owners = self.vm.get_owners_from(city)
        return owners

    def show_car_ownership_history(self, car_id):
        return self.vm.get_car_ownership_history(car_id)

    def change_user_name(self, nid, new_name, new_family_name):
        return self.vm.change_user_name(nid, new_name, new_family_name)

    def change_plate(self, car_id, new_plate):
        return self.vm.change_plate(car_id, new_plate)
    
    def change_ban_status(self, did):
        return self.vm.switch_ban_status(did)
         
    def grant_driver_license(self, user_nid):
        
        user = self.vm.get_user(user_nid)

        if not user: return "User does not exist. Please Register the user first."
        
        driver = self.vm.get_driver(user_nid)
        if driver: return f"{user.name} {user.family_name} is already a driver. driver ID: {driver.did}"
        
        birth_date = user.birth_date.split("-")
        birth_date = datetime(int(birth_date[0]),
                              int(birth_date[1]),
                              int(birth_date[2]))
        
        if self.vm.sys_date - birth_date.date() < timedelta(18 * 365): return "User is not of legal age."
        
        driver_id = generate_eight_digit_id()

        while self.vm.get_driver_did(driver_id):
            driver_id = generate_eight_digit_id()
        
        new_driver = Driver(user.nid,
                            driver_id,
                            self.vm.sys_date)
        
        result = self.vm.add_driver(new_driver)

        if result is True: return f"Driver's license succesfully granted.\nDriver's ID: {driver_id}"


    def add_penalty(self,
                    penalty_id,
                    did,
                    plate_number,
                    penalty_date,
                    penalty_level, 
                    description):
        
        if penalty_id == "":
            penalty_id = str(generate_six_digit_id())

        if not validate_six_digit_id(penalty_id):
            return "Invalid Penalty id. (must be a 6 digit number)"
        
        while self.vm.db.penalties.get(penalty_id):
            penalty_id = str(generate_six_digit_id())
        
        if penalty_level == "0":
            penalty_level = "Low"
        elif penalty_level == "1":
            penalty_level = "Medium"
        elif penalty_level == "2":
            penalty_level = "High"
        else: return "Invalid penalty level."

        if penalty_date == "":
            penalty_date = str(self.vm.sys_date)

        new_penalty = Penalty(
                    penalty_id,
                    did,
                    plate_number,
                    penalty_date,
                    penalty_level,
                    description)
        
        return self.vm.add_penalty(new_penalty)


    