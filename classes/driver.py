from classes.penalty import Penalty
from classes.db.penalties import Penalties
from datetime import datetime, timedelta

class Driver:
    def __init__(self, nid, did, license_date, is_active = True):
        
        self.nid = nid
        self.did = did
        self.license_date = license_date
        self.score = 0
        self.penalties = Penalties()
        self.is_active = True
        self.can_add_plate = True
        self.last_penalty_date = None
        self.end_ban_date = None

    def penalize(self, penalty: Penalty):
        self.penalties.add(penalty)
        self.score -= self.get_penalty_value(penalty.level)
        penalty_date = penalty.date.split("-")

        penalty_datetime = datetime(int(penalty_date[0]),
                                int(penalty_date[1]),
                                int(penalty_date[2]))
        
        if not self.last_penalty_date:
            self.last_penalty_date = penalty_datetime

        elif penalty_datetime > self.last_penalty_date: 
            self.last_penalty_date = penalty_datetime
        
        if self.score < -500: self.is_active = False

        self.end_ban_date = self.last_penalty_date + timedelta(int(self.score/10))

    def get_penalty_value(self, level):
        if level == "Low":
            return 10
        elif level == "Medium":
            return 30
        elif level == "High":
            return 50
        
    def get_all_penalties(self):
        return self.penalties.get_all()
    
    def __repr__(self):
        return f"{self.nid} | {self.did} | {self.license_date} | {self.is_active}"