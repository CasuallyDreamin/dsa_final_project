from file_manager import penalties_file_manager, users_file_manager, cars_file_manager, drivers_file_manager, citycode_file_manager, ownership_history_file_manager

from classes.db import penalties, cars, plates, users, owners, cities, drivers, citycode, ownership_history

from classes.city import City
from classes.user import User
from classes.plate import Plate
from classes.car import Car
from classes.owner import Owner
from classes.driver import Driver
from classes.penalty import Penalty

from classes.ownership_entry import OwnershipEntry
from classes.db.data_structures.sll import sll

class DataBase:
    def __init__(self):
        self.cars = cars.Cars()
        self.plates = plates.Plates()
        self.users = users.Users()
        self.owners = owners.Owners()
        self.cities = cities.Cities()
        self.drivers = drivers.Drivers()
        self.citycode = citycode.CityCode()
        self.penalties = penalties.Penalties()
        self.ownership_history = ownership_history.OwnershipHistory()
        self._read_files()
    
    def add_user(self, user: User):
        return self.users.add(user)

    def add_car(self, car: Car):
        return self.cars.add(car)

    def add_plate(self, plate: Plate):
        city = self.cities.get(plate.number[-2:])
        self.plates.add(plate)
        return city.plates.add(plate)

    def add_driver(self, driver: Driver):
        return self.drivers.add(driver)
    
    def add_penalty(self, new_penalty: Penalty):
        plate = self.plates.get(new_penalty.plate_number)
        driver = self.drivers.get_by_did(new_penalty.did)

        plate.add_penalty(new_penalty)
        driver.penalize(new_penalty)
        return self.penalties.add(new_penalty)

    def get_user(self, nid):
        return self.users.get(nid)
    
    def get_car(self, id):
        return self.cars.get(id)
    
    def get_plate(self, plate_number):
        return self.plates.get(plate_number)
    
    def get_driver(self, nid):
        return self.drivers.get_by_nid(nid)
    
    def get_owner(self, owner_nid):
        return self.owners.get(owner_nid)
    
    def get_driver_did(self, did):
        return self.drivers.get_by_did(did)
        
    def get_all_cars(self):
        return self.cars.get_all()

    def get_all_users(self):
        return self.users.get_all()
    
    def get_all_plates(self):
        return self.plates.get_all()
    
    def get_all_owners(self):
        return self.owners.get_all()
    
    def get_all_drivers(self):
        return self.drivers.get_all()
    
    def delete_car(self, car_id):
        return self.cars.delete(car_id)
    
    def delete_driver(self, nid):
        return self.drivers.delete_nid(nid)
    
    def get_plates_from(self, city):
        city_code = self.citycode.convert_city_to_code(city)
        city = self.cities.get(city_code)
        if city: return city.plates.get_all()
        else: return "City Not Found."

    def get_cars_from(self, city):
        city_code = self.citycode.convert_city_to_code(city)
        city = self.cities.get(city_code)
        if city: return city.cars.get_all()
        else: return "City Not Found."

    def get_cars_between(self, first_year, last_year):
        cars = self.cars.get_all()
        result = sll()
        curr = cars.head
        
        while curr:
            curr_car: Car = curr.data
            if int(first_year) <= int(curr_car.manuf_date) <= int(last_year):
                result.add_first(curr_car)
            curr = curr.next

        return result

    def get_owners_in(self, city):
        city_code = self.citycode.convert_city_to_code(city)
        city = self.cities.get(city_code)
        if city: return city.owners.get_all() 
        else: return "City Not Found."

    def change_user_name(self, nid, new_name, new_family_name):
        c_user = self.get_user(nid)
        if new_name != "": c_user.name = new_name
        if new_family_name != "": c_user.family_name = new_family_name
        return True

    def _read_files(self):
        # add users from file to database

        for _user in users_file_manager.read():
            new_user = User(
                _user[0],
                _user[1],
                _user[2],
                _user[3],
                _user[4]
            )
            if not self.users.add(new_user):
                exit(f"user {_user} was not added.")
        
        for _city in citycode_file_manager.read():
            new_city = City(_city[0], _city[1])
            self.cities.add(new_city)
            self.citycode.add(new_city)

        # Add cars from file to database
        
        for _car in cars_file_manager.read():
            # CarID | CarName | Year | PlateNumber | Color | OwnerNationalID
            new_car = Car(_car[0],
                    _car[1],
                    _car[2],
                    _car[3],
                    _car[4],
                    _car[5])
            
            new_plate = Plate(new_car.plate_number, 
                            new_car.id,
                            new_car.owner_nid
                            )
            
            self.cars.add(new_car)
            self.plates.add(new_plate)
            
            user = self.get_user(new_car.owner_nid)

            if user:
                user.cars.add(new_car)
                user.plates.add(new_plate)
            
            city = self.cities.get(new_car.plate_number[-2:])
            city.cars.add(new_car)
            city.plates.add(new_plate)
            
            curr_owner: Owner = self.owners.get(new_car.owner_nid)
            
            if not curr_owner:
                new_owner: Owner = Owner(new_car.owner_nid)
                new_owner.add_car(new_car)
                city.owners.add(new_owner)
                self.owners.add(new_owner)
            else:
                curr_owner.add_car(new_car)
        # add drivers from file to database

        for _driver in drivers_file_manager.read():
            if _driver[3] == "True": _driver[3] = True
            else: _driver[3] = True
            
            self.drivers.add(
                Driver(
                    _driver[0],
                    _driver[1],
                    _driver[2],
                    _driver[3]
                )
            )

        for _penalty in penalties_file_manager.read():
            new_penalty = Penalty(
                    _penalty[0],
                    _penalty[1],
                    _penalty[2],
                    _penalty[3],
                    _penalty[4],
                    _penalty[5]
                    )
            
            self.penalties.add(new_penalty)

            penalized_driver = self.drivers.get_by_did(new_penalty.did)
            penalized_driver.penalize(new_penalty)

            penalized_plate = self.plates.get(new_penalty.plate_number)
            
            if penalized_plate:
                penalized_plate.add_penalty(new_penalty)

        for _ownership_entry in ownership_history_file_manager.read():
            new_entry = OwnershipEntry(
                    _ownership_entry[0],
                    _ownership_entry[1],
                    _ownership_entry[2],
                    _ownership_entry[3],
                    _ownership_entry[4])
            
            self.ownership_history.add(new_entry)
            
            plate = self.plates.get(new_entry.plate_number)
            
            if plate:
                plate.add_ownership_entry(new_entry)
        
            car = self.cars.get(new_entry.car_id)
            car.add_ownership_entry(new_entry)

    def _write_to_files(self):
        # Read from data structures and write into files to save

        users_file_manager.write(self.users.get_writeable())
        
        citycode_file_manager.write(self.cities.get_writeable())
        
        cars_file_manager.write(self.cars.get_writeable())
        
        drivers_file_manager.write(self.drivers.get_writeable())
        
        penalties_file_manager.write(self.penalties.get_writeable())

        ownership_history_file_manager.write(self.ownership_history.get_writeable())

    def save(self):
        self._write_to_files()

db = DataBase()