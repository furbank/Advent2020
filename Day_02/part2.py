with open("Day_02\input.txt") as f:
    content = f.read().splitlines()

#content = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']

def check_pw( line ):
    rule_min = int((line.split())[0].split('-')[0]) -1
    rule_max = int((line.split())[0].split('-')[1]) -1
    rule = (line.split())[1][:1]
    pw = (line.split())[2]

    return ((pw[rule_min] == rule) != (pw[rule_max] == rule))

n=0
for x in content:
    if check_pw(x): n += 1

print(n)

