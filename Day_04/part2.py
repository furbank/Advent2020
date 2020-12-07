with open("Day_04\input.txt") as f:
    data = f.read().split('\n\n')

# check for and remove trailing whitespace
data[-1] = data[-1].rstrip()

# "tidy" data
data = [c.replace('\n',' ') for c in data]
data = [c.split(' ') for c in data]

# get list of dictionaries
data = [dict([(kv.split(':')[0],kv.split(':')[1]) for kv in passport if kv.split(':')[0] != 'cid']) for passport in data]

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

def check_year(value_year, min_year, max_year):
    if value_year.isnumeric():
        if min_year <= int(value_year) <= max_year:
            return True
    return False

def check_hight(value_hight):
    unit = value_hight[-2:]
    hight = value_hight[:-2]

    if hight.isnumeric():
        if unit == 'cm' and 150 <= int(hight) <= 193:
            return True
        elif unit == 'in' and 59 <= int(hight) <= 76:
            return True
    return False

def check_hair(value_hair):
    import re

    m = re.match('^#[0-9a-f]{6}$', value_hair)
    if m and m.group() == value_hair:
        return True
    return False

def check_eyes(value_eyes):
    return value_eyes in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def check_pid(value_pid):
    return value_pid.isnumeric() and len(value_pid) == 9

def check_passport(data):
    return all([
            check_year(data['byr'], 1920, 2002),
            check_year(data['iyr'], 2010, 2020),
            check_year(data['eyr'], 2020, 2030),
            check_hight(data['hgt']),
            check_hair(data['hcl']),
            check_eyes(data['ecl']),
            check_pid(data['pid'])
    ])

print(len([d for d in data if len(d) == 7 and check_passport(d)]))

