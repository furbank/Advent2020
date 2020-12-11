with open("Day_09\input") as f:
    data = f.read().splitlines()
data = list(enumerate([int(d) for d in data]))

preamble = 25

for d in [d for d in data[preamble:]]:
    offset = d[0]
    check = d[1]
    candidates = (set([a[1] +b[1] for b in data[offset-preamble:offset] for a in data[offset-preamble:offset] if a[0] != b[0]]))

    if check not in candidates:
        print('First no match:', d[1], 'at position:', d[0])
        break
