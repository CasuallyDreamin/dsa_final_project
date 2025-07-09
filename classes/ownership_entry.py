class OwnershipEntry:
    def __init__(self,
                car_id,
                owner_nid,
                start_date,
                end_date,
                plate_number):
        
        self.car_id = car_id
        self.owner_nid = owner_nid
        self.start_date = start_date
        self.end_date = end_date
        self.plate_number = plate_number

    def __repr__(self):
        return f"{self.car_id} | {self.owner_nid} | {self.start_date} | {self.end_date} | {self.plate_number}"