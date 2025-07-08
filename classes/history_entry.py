class History_entry:
    def __init__(self, car_id, owner_nid, date):
        self.car_id = car_id
        self.owner_nid = owner_nid
        self.date = date

    def __repr__(self):
        return f"{self.car_id} | {self.owner_nid} | {self.date}"