from db.data_structures.hashtable import hashtable
from classes.city import City

class Cities:
    def __init__(self):
        self.cities = hashtable()

    def add(self, city):
        self.cities.insert(city.code, city)
        return True
    
    def get(self, code):
        return self.cities.get(code)
    
    def get_cars_in(self, city_code):
        city: City = self.get(city_code)

        if not city:
            return False
        
        return city.cars.get_all()

        
