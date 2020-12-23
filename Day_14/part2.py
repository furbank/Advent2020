with open("Day_14\input") as f:
    data = f.read().splitlines()

# Test data from problem
# data = [
#     'mask = 000000000000000000000000000000X1001X',
#     'mem[42] = 100',
#     'mask = 00000000000000000000000000000000X0XX',
#     'mem[26] = 1',
# ]

# Parse input into list of instructions: Address, Value, Memory Address Decoder
mad = ''
instructions = []
for d in data:
    if d[:4] == 'mask':
        mad = d[7:]
    else:
        instructions.append([int(d[4:d.index(']')]), int(d[d.rindex(' '):]), mad])

# Expand instructions to full address space and write to memory
PosibleBits = lambda m: [bin(f)[2:].zfill(m.count('X')) for f in range(2**m.count('X'))]
RootAddress = lambda a, m: a & int(m.replace('0', '1').replace('X', '0'),2)

mem = {} # Simulate memory as dictionary
for i in instructions:
    mask = ''
    for pb in PosibleBits(i[2]):
        mask = i[2]
        [mask := mask.replace('X', b, 1) for b in pb]
        mem[int(mask,2) | RootAddress(i[0], i[2])] = i[1]

# Sum all remaining memory values
print(sum(mem.values()))

