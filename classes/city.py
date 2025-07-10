from .db.cars import Cars
from .db.users import Users
from .db.owners import Owners
from .db.plates import Plates

class City:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.cars = Cars()
        self.plates = Plates()
        self.owners = Owners()
        self.users = Users()

    def __repr__(self):
        return f"{self.code} | {self.name}"
