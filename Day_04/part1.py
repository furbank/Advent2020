with open("Day_04\input.txt") as f:
    data = f.read().split('\n\n')

# check for and remove trailing whitespace
data[-1] = data[-1].rstrip()

# "tidy" data
data = [c.replace('\n',' ') for c in data]
data = [c.split(' ') for c in data]

# get list of keys (filter out cid keys)
data = [[kv.split(':')[0] for kv in passport if kv.split(':')[0] != 'cid'] for passport in data]

# get count of lists with 7 items

print(len([keys for keys in data if len(keys) == 7]))



# test = ['iyr:2013', 'hcl:#ceb3a1', 'hgt:151cm', 'eyr:2030', 'byr:1943', 'ecl:grn']
# test = [(t.split(':')[0]) for t in test if t.split(':')[0] != 'hcl']
# #test.sort()
# print(test)


