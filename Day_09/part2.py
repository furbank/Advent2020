with open("Day_09\input") as f:
    data = f.read().splitlines()

data = list(enumerate([int(d) for d in data]))

preamble = 25

for d in [d for d in data[preamble:]]:
    if d[1] not in (set([a[1] + b[1] for b in data[d[0]-preamble:d[0]] for a in data[d[0]-preamble:d[0]] if a[0] != b[0]])):
        noMatch = d[1]
        noMatchPos = d[0]
        break

print('First no match:', noMatch, 'at input line:', noMatchPos + 1)

for x in data:
    for y in data[x[0]+2:]:
        checkRange = [d[1] for d in data[x[0]:y[0]]]
        if sum(checkRange) >= noMatch:
            break
    if sum(checkRange) == noMatch:
        break

print('Encryption weakness:', min(checkRange) + max(checkRange))
