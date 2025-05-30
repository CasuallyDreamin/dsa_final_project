from .base_ui import ui

class ap_ui(ui):
    def __init__(self):
        menu = """
1. register a car
2. show all cars
3. show all users
4. show plates in city
5. show cars in city
6. show owners in city
7. show cars manufactured in time period
8. change user name
"""
        options = [1 , 2, 3, 4, 5, 6, 7, 8]
        super().__init__(options, menu)