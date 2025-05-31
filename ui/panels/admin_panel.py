from classes.car import car

class AdminPanel:
    def __init__(self, vm):
        self.curr_user = vm.curr_user
        self.vm = vm

    def register_car(self,
                color,
                name,
                manuf_date,
                car_id,
                plate,
                plate_date):
        
        # TODO register car return True or False for the UI
        ...

    def show_all_cars(self):
        ...

    def show_all_users(self):
        
        ...

    def show_plates_in(self, city):
        # plate - active/inactive 
        ...

    def show_cars_in(self, city):
        # color - name - date - plate - car_id - owner_id   
        ...

    def show_cars_between(self, 
                        first_year = None,
                        last_year  = None):
        # show cars in manufactured date period
        # name - manufactured date - color - plate
        ...

    def show_all_owners_in(self, city):
        # all user infos that live in the city and have an active plate
        ...

    def change_user_name(self, new_name, new_family_name):
        ...

    