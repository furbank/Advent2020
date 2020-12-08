from collections import Counter

with open("Day_06\input") as f:
    data = f.read().split('\n\n')

# check for and remove trailing whitespace
data[-1] = data[-1].rstrip()
data = [d.replace('\n','-') + '-' for d in data]
data = [Counter(d) for d in data]

data = [len([x for x in d.items() if x[1] == d['-'] and x[0] != '-']) for d in data]
print(sum(data))
