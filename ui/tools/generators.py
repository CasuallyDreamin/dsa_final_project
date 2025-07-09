from random import randint, choice
from classes.db.data_structures.arr import arr

def generate_plate(citycode):
    
    while True:
        alpha = choice("ABCEFGHIJKLMNOQRSTUVWXYZ")
        first_two_digits = str(randint(10,99))
        last_three_digits = str(randint(100,999))
        
        f2 = arr(2)
        l3 = arr(3)

        for i in range(2): f2.insert(i, first_two_digits[i])
        
        for i in range(3): l3.insert(i, last_three_digits[i])
        
        if alpha == "X":
            for i in range(2):
                if int(f2.get(i)) % 2 == 0:
                    f2.insert(i, str(int(f2.get(i)) + 1))

            for i in range(3):
                if int(l3.get(i)) % 2 == 0:
                    l3.insert(i , str(int(l3.get(i)) + 1)) 
        plate = ""
        for i in range(2): plate += f2.get(i)
        for i in range(3): plate += l3.get(i)
        
        if plate == plate[0] * 5: continue    
        if is_sorted(plate): continue
        
        return f"{plate[:2]}{alpha}{plate[2:]}-{citycode}"

def generate_six_digit_id():
    return randint(100000, 999999)

def is_sorted(string: str):
    is_desc = True
    is_asc = True
    
    for i in range(len(string) - 1):
        if not string[i].isnumeric(): return False
        if int(string[i]) < int(string[i + 1]): is_desc = False
        if int(string[i]) > int(string[i + 1]): is_asc = False

    return not is_desc and not is_asc