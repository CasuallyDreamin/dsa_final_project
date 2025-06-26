from classes.car import Car

class AdminPanel:
    def __init__(self, vm):
        self.vm = vm

    def plate_car(self,
                color,
                name,
                manuf_date,
                car_id,
                plate,
                plate_date):
        
        # TODO register car return True or False for the UI
        new_car = Car(
                name,
                color,
                manuf_date,
                car_id,
                plate)
        
        return self.vm.plate_car(new_car, plate_date)
        
    def show_all_cars(self):
        # all_cars = self.vm.get_all_cars()
        # TODO: return the string version of all cars.
        return "All Cars!"

    def show_all_users(self):
        # all_users = self.vm.get_all_users()
        # TODO: return the string version of all cars.
        return "All users!"

    def show_plates_in(self, city):
        # plates = self.vm.get_plates_from(city)
        # plate - active/inactive 
        return f"Plates from {city}!"

    def show_cars_in(self, city):
        # cars = self.vm.get_cars_from(city) 
        # color - name - date - plate - car_id - owner_id   
        return f"Cars from {city}!"

    def show_cars_between(self, 
                        first_year = None,
                        last_year  = None):
        # cars = self.vm.get_cars_between(first_year, last_year)
        # show cars in manufactured date period
        # name - manufactured date - color - plate
        return f"cars made from {first_year} to {last_year}"

    def show_owners_in(self, city):
        # owners = self.vm.get_owners_from(city)
        # all user infos that live in the city and have an active plate
        return f"owners in {city}"

    def change_user_name(self, nid, new_name, new_family_name):
        return self.vm.change_user_name(nid, new_name, new_family_name)

    