from .data_structures.hashtable import hashtable
from classes.car import Car
class Cars:
    def __init__(self):
        self.ht = hashtable()
        self.size = 0
        
    def add(self, car):
        self.size += 1
        return self.ht.insert(car.id, car)
        
    def get(self, car_id: str)-> Car:
        return self.ht.get(car_id)

    def delete(self, car_id):
        return self.ht.delete(car_id)
    
    def exists(self, car_id: str):
        if self.get_user(car_id): return True
        else: return False

    def get_all(self):
        return self.ht.get_all()

    def get_writeable(self):
        return self.__repr__()
    
    def __repr__(self):
        return "CarID | CarName | Year | PlateNumber | Color | OwnerNationalID\n" + str(self.ht.get_all())