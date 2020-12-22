with open("Day_14\input") as f:
    data = f.read().splitlines()

mask = ''
instructions = []
for d in data:
    if d[:4] == 'mask':
        mask = d[7:]
    else:
        instructions.append([int(d[4:d.index(']')]), int(d[d.rindex(' '):]), mask])

[print(i) for i in instructions]