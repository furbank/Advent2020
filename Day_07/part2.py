with open("Day_07\input") as f:
    data = f.read().splitlines()

# clean data
data = [d.split(' bags contain ') for d in data]
#data = [[d[0], '0 ' + d[1][2:] if 'no other' in d[1] else d[1]] for d in
data = [[d[0], d[1].replace('no other', '0 other')] for d in data]
data = [[d[0], d[1][:-1].replace(' bags', '').replace(' bag', '').split(', ')] for d in data]

# expand rules to 1 per list element
rules = []
[[rules.append([d[0], int(r[0]), r[2:]]) for r in d[1]] for d in data]

totalBags = 0
myBag = 'shiny gold'
bags = [r for r in rules if r[0] == myBag]

while bags:
    b = bags.pop()
    totalBags += b[1]

    for r in [r for r in rules if r[0] == b[-1]]:
        if r[1] !=0: bags.append([r[0], (b[1]*r[1]), r[2]])

print(totalBags)
