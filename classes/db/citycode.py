from classes.db.data_structures.hashtable import hashtable

class CityCode:
    def __init__(self):
        self.cities = hashtable()
    
    def add(self, city):
        self.cities.insert(city.name, city.code)

    def convert_city_to_code(self, city):
        return self.cities.get(city)
