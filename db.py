from .classes.db import cars, plates, users
from .classes import car, user, plate

class DataBase:
    def __init__(self):
        self.cars = cars.cars()
        self.plates = plates.plates()
        self.users = users.Users()

    def add_user(self, user: user):
        return self.users.add(user)

    def add_car(self, car: car):
        return self.cars.add(car)

    def add_plate(self, plate: plate):
        return self.plates.add(plate)