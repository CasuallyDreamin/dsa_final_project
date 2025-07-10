from .data_structures.hashtable import hashtable
from classes.city import City

class Cities:
    def __init__(self):
        self.cities = hashtable()

    def add(self, new_city: City):
        return self.cities.insert(new_city.code, new_city)
        
    
    def get(self, code)-> City:
        return self.cities.get(code)
    
    def get_all(self):
        return self.cities.get_all()
    
    def get_cars_in(self, city_code):
        city: City = self.get(city_code)

        if not city:
            return False
        
        return city.cars.get_all()
    
    def __repr__(self):
        return "CityCode | CityName\n" + self.get_all()
        

        
