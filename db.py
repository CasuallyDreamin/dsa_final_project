from classes.db import cars, plates, users
from classes import car, user, plate

class DataBase:
    def __init__(self):
        self.cars = cars.Cars()
        self.plates = plates.Plates()
        self.users = users.Users()

    def add_user(self, user: user.User):
        return self.users.add(user)

    def add_car(self, car: car.Car):
        return self.cars.add(car)

    def add_plate(self, plate: plate.Plate):
        return self.plates.add(plate)
    
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
    
    def add_user(self, new_user):
        return self.db.add_user(new_user)
    
    def login(self, national_id, password):
        return self.db.login(national_id, password)
    
    def add_plate(self, new_plate):
        return self.db.add_plate(new_plate)  