from .base_ui import UI
from .panels.user_panel import UserPanel
from clear_screen import clear
from .tools.validators import validate_nid, validate_password, validate_date
from sys import exit

class UserPanelUI(UI):
    def __init__(self, vm):
        menu = """
1. register
2. login
3. create a plate
4. see your cars
5. see your plates
6. see negative points
7. see your record
8. see plate record
9. see plate ownership history
0. return
"""
        options = 10
        super().__init__(options, menu, vm)
        self.panel = UserPanel(vm)

    def do_task(self, task_id):
        if task_id == "1": self.register()
        elif task_id == "2": self.login()
        elif task_id == "3": self.create_plate()
        elif task_id == "4": self.see_all_cars()
        elif task_id == "5": self.see_all_plates()
        elif task_id == "6": self.see_negative_points()
        elif task_id == "7": self.get_user_record()
        elif task_id == "8": self.get_plate_record()
        elif task_id == "9": self.get_plate_ownership_history()
        elif task_id == "0": self.running = False

    def register(self):
        clear()
        
        name = input("Name: ")
        
        family_name = input("Family name: ")
        
        birth_date = input("Enter birth date YYYY-MM-DD: ")
        if not validate_date(birth_date): return input("Invalid date.")
    
        national_id = input("National ID: ")
        if not validate_nid(national_id): return input("Invalid national ID.")

        password = input("Password:")
        if not validate_password(password): return input("Invalid password.")

        if self.panel.register( 
                national_id,
                name,
                family_name,
                birth_date,
                password
        ): input("Successfully registered.")
        else: input("National ID already exists.")

    def login(self):
        clear()

        national_id = input("National ID: ")
        if not validate_nid(national_id): return input("Invalid national ID.")

        password = input("Password: ")
        if not validate_password(password): return input("Invalid Password.")

        if self.panel.login(national_id, password): input("Successfully logged in.")
        else: input("Wrong national ID or password.")

    def create_plate(self):
        city = input("Enter city:")
        input(self.panel.create_plate(city))        

    def see_all_cars(self):
        input(self.panel.get_user_cars())

    def see_all_plates(self):
        input(self.panel.get_user_plates())

    def see_negative_points(self):
        input(self.panel.get_negative_points())        

    def get_user_record(self):
        input(self.panel.get_user_record())

    def get_plate_record(self):
        plate = input("Plate number: ")

        input(self.panel.get_plate_record(plate))
    
    def get_plate_ownership_history(self):
        plate = input("Plate number: ")

        input(self.panel.get_plate_ownership_history(plate))