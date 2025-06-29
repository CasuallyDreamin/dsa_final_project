class Plate:
    def __init__(self, plate_number, car_id = None, user_id = None):
        self.plate_number = plate_number
        self.car_id = car_id
        self.user_id = None

    def __repr__(self):
        return f"{self.plate_number} | {self.car_id} | {self.user_id}"