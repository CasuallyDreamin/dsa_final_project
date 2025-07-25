from .base_ui import UI
from .panels.admin_panel import AdminPanel
from .tools.validators import validate_year, validate_plate, validate_color, validate_date 
from viewmodel import ViewModel

class AdminPanelUI(UI):
    def __init__(self, vm: ViewModel):
        menu = """
1. plate a car
2. see all cars
3. see all users
4. see all plates
5. see all owners
6. see all drivers
7. see plates in city
8. see cars in city
9. see owners in city
10. see cars manufactured in time period
11. see car ownership history
12. change car plate
13. change user name
14. delete car
15. delete drivers license    
16. grant driver license
17. ban/unban driver
18. penalize driver
19. get owners with more cars than x
0. return
"""     
        options = 20
        super().__init__(options, menu, vm)
        self.panel = AdminPanel(vm)

    def do_task(self, task_id):
        if task_id == "1": self.plate_car()
        elif task_id == "2": self.see_all_cars()
        elif task_id == "3": self.see_all_users()
        elif task_id == "4": self.see_all_plates()
        elif task_id == "5": self.see_all_owners()
        elif task_id == "6": self.see_all_drivers()
        elif task_id == "7": self.see_plates_city_filtered()
        elif task_id == "8": self.see_cars_city_filtered()
        elif task_id == "9": self.see_owners_city_filtered()
        elif task_id == "10": self.see_cars_manufdate_filtered()
        elif task_id == "11": self.see_car_ownership_history()
        elif task_id == "12": self.change_car_plate()
        elif task_id == "13": self.change_user_name()
        elif task_id == "14": self.delete_car()
        elif task_id == "15": self.delete_drivers_license()
        elif task_id == "16": self.grant_drivers_license()
        elif task_id == "17": self.ban_unban_driver()
        elif task_id == "18": self.penalize_driver()
        elif task_id == "19": self.get_owners_with_more_cars()
        elif task_id == "0": self.running = False

    def get_owners_with_more_cars(self):
        x: str = input("x: ")

        if not x.isalnum():
            return input("must enter a number")

        input(self.panel.get_owners_with_more_cars(x))
        
    def plate_car(self):
        color = input("Color \nWT: White | BC: Black | RD: Red | BL: Blue | GR: Green | OT: Other): ")
        if not validate_color(color): return input("Invalid Color.")

        name = input("Name: ")
        
        manuf_date = input("Manufactured year YYYY: ")
        if not validate_year(manuf_date): return input("Invalid year.")

        car_id = input("Car ID: ")

        plate = input("Plate: ")
        if not validate_plate(plate): return input("Invalid Plate.")

        plate_date = input("Plate Date (YYYY-MM-DD) leave blank to use system data.")
        if not validate_date(plate_date) and plate_date != "": return input("Invalid Plate Date.")

        if self.panel.plate_car(
            color,
            name,
            manuf_date,
            car_id,
            plate,
            plate_date
        ): input("Successfully registered the car.")
        else: input("Car ID already exists.")
        
    def see_all_cars(self):
        input(self.panel.show_all_cars())

    def see_all_users(self):
        input(self.panel.show_all_users())
    
    def see_all_plates(self):
        input(self.panel.show_all_plates())

    def see_all_owners(self):
        input(self.panel.show_all_owners())
    
    def see_all_drivers(self):
        input(self.panel.show_all_drivers())

    def see_plates_city_filtered(self):
        city = input("City: ")
        input(self.panel.show_plates_in(city))

    def see_cars_city_filtered(self):
        city = input("City: ")
        input(self.panel.show_cars_in(city))

    def see_owners_city_filtered(self):
        city = input("City: ")
        input(self.panel.show_owners_in(city))

    def see_cars_manufdate_filtered(self):
        first_year = input("from(YYYY): ")
        last_year = input("To(YYYY): ")
        
        if not (validate_year(first_year) or validate_year(last_year)):
            return input("Invalid format for years.")

        input(self.panel.show_cars_between(first_year, last_year))
    
    def see_car_ownership_history(self):
        car_id = input("Car ID: ")
        input(self.panel.show_car_ownership_history(car_id))


    def change_car_plate(self):
        car_id = input("Car ID: ")
        car = self.panel.vm.get_car(car_id)
        
        if not car: return input("Car was not found.")
        
        print("CarID | CarName | Year | PlateNumber | Color | OwnerNationalID")
        print(car)
        
        new_plate = input("New plate: ") 
        input(self.panel.change_plate(car_id, new_plate))

    
    def change_user_name(self):
       nid = input("National ID: ")
       user = self.vm.get_user(nid)
       
       if not user: return input("User not found!")
       
       print(f"{user.name} {user.family_name}")        
       new_name = input("New Name (Leave blank to keep old name):")
       new_family_name = input("New Family Name (leave blank to keep the old one):")
       
       return self.panel.change_user_name(nid, new_name, new_family_name)
    
    def delete_car(self):
        car_id = input("Car ID: ")
        input(self.panel.delete_car(car_id))
    
    def delete_drivers_license(self):
        nid = input("National ID: ")
        input(self.panel.delete_driver(nid))
    
    def grant_drivers_license(self):
        nid = input("National ID: ")
        input(self.panel.grant_driver_license(nid))
    
    def ban_unban_driver(self):
        nid = input("National ID: ")
        input(self.panel.change_ban_status(nid))

    def penalize_driver(self):
        driver_id = input("Driver ID: ")
        plate_number = input("Plate: ")
        penalty_date = input("Offense date (Leave blank to use system date): ")
        offense_level = input("Offense level (0: Low | 1: Medium | 2: High): ")
        description = input("Description: ")
        
        input(self.panel.add_penalty(
            '',
            driver_id,
            plate_number,
            penalty_date,
            offense_level,
            description
        ))
