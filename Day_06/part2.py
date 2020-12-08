with open("Day_06\input") as f:
    data = f.read().split('\n\n')

# check for and remove trailing whitespace
data[-1] = data[-1].rstrip()

print(sum([len(set(d.replace('\n',''))) for d in data]))