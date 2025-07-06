from classes.db import penalties, cars, plates, users, owners, cities, drivers, citycode
from classes import car, user, plate, owner, driver, penalty
from file_manager import penalties_file_manager, users_file_manager, cars_file_manager, drivers_file_manager, citycode_file_manager
from classes.city import City
from classes.user import User
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
        self.read_files()

    def read_files(self):
        # add users from file to database

        for _user in users_file_manager.read():
            new_user = User(
                _user[0],
                _user[1],
                _user[2],
                _user[3],
                _user[4]
            )
            self.users.add(new_user)
        
        for _city in citycode_file_manager.read():
            new_city = City(_city[0], _city[1])
            self.cities.add(new_city)
            self.citycode.add(new_city)

        # Add cars from file to database
        
        for _car in cars_file_manager.read():
            # CarID | CarName | Year | PlateNumber | Color | OwnerNationalID
            new_car = car.Car(_car[0],
                    _car[1],
                    _car[2],
                    _car[3],
                    _car[4],
                    _car[5])
            new_plate = plate.Plate(new_car.plate_number, 
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
            
            new_owner = owner.Owner(new_car.owner_nid)
            new_owner.cars.add(new_car)
            city.owners.add(new_owner)
            self.owners.add(new_owner)

        # add drivers from file to database

        for _driver in drivers_file_manager.read():
            self.drivers.add(
                driver.Driver(
                    _driver[0],
                    _driver[1],
                    _driver[2]
                )
            )

        for _penalty in penalties_file_manager.read():
            self.penalties.add(
                penalty.Penalty(
                    _penalty[0],
                    _penalty[1],
                    _penalty[2],
                    _penalty[3],
                    _penalty[4],
                    _penalty[5]
                )
            )

    def add_user(self, user: user.User):
        return self.users.add(user)

    def add_car(self, car: car.Car):
        return self.cars.add(car)

    def add_plate(self, plate: plate.Plate):
        city = self.cities.get(plate.number[-2:])
        city.plates.add(plate)
        return self.plates.add(plate)
    
    def get_user(self, nid):
        return self.users.get(nid)
    
    def get_car(self, id):
        return self.cars.get(id)
    
    def get_plate(self, plate_number):
        return self.plates.get(plate_number)
    
    def get_all_cars(self):
        return self.cars.get_all()

    def get_all_users(self):
        return self.users.get_all()
    
    def get_all_plates(self):
        return self.plates.get_all()
    
    def get_plates_from(self, city):
        city_code = self.citycode.convert_city_to_code(city)
        city = self.cities.get(city_code)
        return city.plates.get_all()

    def get_cars_from(self, city):
        city_code = self.citycode.convert_city_to_code(city)
        city = self.cities.get(city_code)
        return city.cars.get_all()

    def get_cars_between(self, first_year, last_year):
        cars = self.cars.get_all()
        result = sll()
        curr = cars.head
        
        while curr:
            curr_car: car.Car = curr.data
            if int(first_year) <= int(curr_car.manuf_date) <= int(last_year):
                result.add_first(curr_car)
            curr = curr.next

        return result

    def get_owners_in(self, city):
        city_code = self.citycode.convert_city_to_code(city)
        city = self.cities.get(city_code)
        return city.owners.get_all()
    
    def change_user_name(self, nid, new_name, new_family_name):
        c_user = self.get_user(nid)
        if new_name != "": c_user.name = new_name
        if new_family_name != "": c_user.family_name = new_family_name
        return True

db = DataBase()