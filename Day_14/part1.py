with open("Day_14\input") as f:
    data = f.read().splitlines()

ApplyMask = lambda v, m: (v | int(m.replace('X', '0'),2)) & int(m.replace('X', '1'),2)

mask = ''
instructions = {}
for d in data:
    if d[:4] == 'mask':
        mask = d[7:]
    else:
        instructions[int(d[4:d.index(']')])] = ApplyMask( int(d[d.rindex(' '):]), mask)

print(sum(instructions.values()))
