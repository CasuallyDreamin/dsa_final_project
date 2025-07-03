class Plate:
    def __init__(self, plate_number, car_id = None, owner_nid = None):
        self.number = plate_number
        self.car_id = car_id
        self.owner_nid = owner_nid

    def __repr__(self):
        return f"{self.number} | {self.car_id} | {self.owner_nid}"