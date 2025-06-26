class User:
    def __init__(self,
                 name,
                 family_name,
                 birth_date,
                 national_id,
                 password,
                 cars = None):
        
        self.name        = name
        self.family_name = family_name
        self.birth_date  = birth_date
        self.national_id = national_id
        self.password    = password
        self.cars        = cars
        
        