from .base_ui import ui

class up_ui(ui):
    def __init__(self):
        menu = """
1. register
2. login
3. create a plate
4. see all cars
5. see all plates
"""
        options = [1 , 2]
        super().__init__(options, menu)