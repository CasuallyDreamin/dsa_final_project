from random import randint, choice

def generate_plate(citycode):
    while True:
        alpha = choice("ABCEFGHIJKLMNOQRSTUVWXYZ")
        first_two_digits = str(randint(10,99))
        last_three_digits = str(randint(100,999))
        
        if alpha == "X":
            for i in range(len(first_two_digits)):
                if int(first_two_digits[i]) % 2 == 0:
                    first_two_digits[i] = str(first_two_digits[i] + 1)

            for i in range(len(last_three_digits)):
                if int(last_three_digits[i]) % 2 == 0:
                    last_three_digits[i] = str(last_three_digits[i] + 1)

        if first_two_digits + last_three_digits == first_two_digits[0] * 5: continue    
        if is_sorted(first_two_digits + last_three_digits): continue
        
        return f"{first_two_digits}{alpha}{last_three_digits}-{citycode}"

def is_sorted(string: str):
    is_desc = True
    is_asc = True
    
    for i in range(len(string) - 1):
        if not string[i].isnumeric(): return False
        if string[i] < string[i + 1]: is_desc = False
        if string[i] > string[i + 1]: is_asc = False

    return not (is_desc or is_asc)