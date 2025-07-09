from classes.car import Car
from viewmodel import ViewModel
from datetime import datetime

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
        # TODO: Change plate activity to inactive
        return self.vm.delete_car(car_id)
    
    def delete_driver(self, nid):
        # TODO: Remove user from drivers
        return 
    
    def show_plates_in(self, city):
        plates = self.vm.get_plates_from(city)
        # plate - active/inactive 
        return str(plates)

    def show_cars_in(self, city):
        cars = self.vm.get_cars_from(city) 
        # color - name - date - plate - car_id - owner_id   
        return str(cars)

    def show_cars_between(self, 
                        first_year = None,
                        last_year  = None):
        cars = self.vm.get_cars_between(first_year, last_year)
        # show cars in manufactured date period
        # name - manufactured date - color - plate
        return cars

    def show_owners_in(self, city):
        owners = self.vm.get_owners_from(city)
        # all user infos that live in the city and have an active plate
        return owners

    def show_car_ownership_history(self, car_id):
        # TODO: return ownership history of the car
        # owner NID - owning start date - owning end date - plate number
        return

    def change_user_name(self, nid, new_name, new_family_name):
        return self.vm.change_user_name(nid, new_name, new_family_name)

    def change_plate(self, car_id, new_plate):
        # TODO: change plate of car to new plate
        return
    
    def change_ban_status(self, did):
        # TODO: change driver license activity (active/inactive)
        return 
    
    def grant_driver_license(self, user_nid):
        # TODO: turn user into driver
        # if doesn't exist, make the user first
        return 

    def add_penalty(self, penalty_id, did, plate_number, penalty_date, penalty_level, description):
        # TODO: add penalty to the system
        return


    