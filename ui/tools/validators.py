from datetime import datetime

def validate_plate(plate: str):
    plate = plate.split("-")
    if len(plate) != 2: return False
    if len(plate[1]) != 2 or not plate[1].isnumeric(): return False
    if len(plate[0]) != 6: return False

    return plate[0][2].isalpha() and plate[0][:2].isnumeric() and plate[0][3:].isnumeric()

def validate_nid(national_id: str):
    return national_id.isalnum() and len(national_id) == 10

def validate_color(color: str):
    return color in ['WT','BC','RD','BL','GR','OT']

def validate_date(date: str):
    date = date.split("-")

    if len(date) != 3: return False
    
    try: datetime(int(date[0]), int(date[1]), int(date[2]))
    except: return False

    return True

def validate_password(password: str):
    has_num = False
    has_alpha = False
    is_eight_digits = len(password) == 8

    for char in password:
        if char.isdigit(): has_num = True
        if char.isalpha(): has_alpha = True
    
    return has_num and has_alpha and is_eight_digits

def validate_year(year: str):
    if len(year) != 4:
         return False
    
    try:
        return 1900 <= int(year) <= 2100
    except: return False      

