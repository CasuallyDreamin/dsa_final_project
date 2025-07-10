class Penalty:
    def __init__(self,
            id, 
            did, 
            plate_number, 
            date, 
            level, 
            description):
        
        self.id: str = id
        self.did: str = did
        self.plate_number: str = plate_number
        self.date: str = date
        self.level: str = level
        self.description: str = description
    
    def __repr__(self):
        return f"{self.id} | {self.did} | {self.plate_number} | {self.date} | {self.level} | {self.description}"