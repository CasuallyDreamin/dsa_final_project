from .data_structures.hashtable import hashtable

class Cars:
    def __init__(self):
        self.ht = hashtable()
        
    def add(self, car):
        return self.ht.insert(car.id, car)
        
    def get(self, car_id: str):
        return self.ht.get(car_id)

    def exists(self, car_id: str):
        if self.get_user(car_id): return True
        else: return False

    def get_all(self):
        return self.ht.get_all()
