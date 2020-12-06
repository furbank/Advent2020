with open("Day_02\input.txt") as f:
    content = f.read().splitlines()

def check_pw( line ):
    rule_min = (line.split())[0].split('-')[0]
    rule_max = (line.split())[0].split('-')[1]
    rule = (line.split())[1][:1]
    pw = (line.split())[2]

    return int(rule_min) <= pw.count(rule) <= int(rule_max)

n=0
for x in content:
    if check_pw(x): n += 1

print(n)

