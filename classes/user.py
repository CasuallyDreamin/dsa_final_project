class User:
    def __init__(self,
                 nid,
                 name,
                 family_name,
                 birth_date,
                 password):
        
        self.nid = nid
        self.name        = name
        self.family_name = family_name
        self.birth_date  = birth_date
        self.password    = password
        
    def __repr__(self):
        return f"{self.nid} | {self.name} | {self.family_name} | {self.birth_date} | {self.password}"