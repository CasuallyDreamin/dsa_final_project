class Car:
    def __init__(self,
                 name,
                 manuf_date,
                 id,
                 plate,
                 color,
                 owner_nid):
        
        self.id           = id
        self.name         = name
        self.manuf_date   = manuf_date
        self.plate_number = plate
        self.color        = color
        self.owner_nid = owner_nid

    def __repr__(self):
        return f"{self.id} | {self.name} | {self.manuf_date} | {self.plate_number} | {self.color} | {self.owner_nid}"
