with open("Day_13\input") as f:
    data = f.read().splitlines()

#data = ['939', '7,13,x,x,59,x,31,19']

target = {}
offset = 0

for d in data[1].split(','):
    if d.isnumeric():
        target[offset] = int(d)
        print(f'{offset:>}: {d}')
    offset += 1
