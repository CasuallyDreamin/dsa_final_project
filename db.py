from classes.db import penalties, cars, plates, users, owners, cities, drivers, citycode
from classes import car, user, plate, owner, driver, city, penalty
from file_manager import penalties_file_manager, users_file_manager, cars_file_manager, drivers_file_manager, citycode_file_manager

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
            self.users.add(
                user.User(_user[0],
                    _user[1],
                    _user[2],
                    _user[3],
                    _user[4])
            )
        
        for _city in citycode_file_manager.read():
            self.cities.add(
                city.City(_city[0],
                          _city[1])
            )

        # Add cars from file to database
        
        for _car in cars_file_manager.read():
            new_car = car.Car(_car[0],
                    _car[1],
                    _car[2],
                    _car[3],
                    _car[4],
                    _car[5])
            
            self.cars.add(new_car)

            city = self.cities.get(new_car.plate_number[-2:])
            city.cars.add(new_car)

            new_owner = owner.Owner(new_car.owner_nid)
            new_owner.cars.add(new_car)
            self.owners.add(new_owner)
            city.owners.add(new_owner)

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
        return self.plates.add(plate)
    
    def get_user(self, nid):
        return self.users.get(nid)
    
    def get_car(self, id):
        return self.cars.get(id)
    
    def get_plates(self, plate_number):
        return self.plates.get(plate_number)
    
    def get_all_cars(self):
        return self.cars.get_all()

    def get_all_users(self):
        return self.users.get_all()

    def get_plates_from(self, city):
        self.plates.get_by_city(city)

    def get_cars_from(self, city):
        return self.db.get_cars_from(city)

    def get_cars_between(self, first_year, last_year):
        return self.db.get_cars_between(first_year, last_year)
    
    def get_owners_in(self, city):
        return self.db.get_owners_in(city)
    
    def change_user_name(self, nid, new_name, new_family_name):
        return self.db.change_user_name(nid, new_name, new_family_name)
      