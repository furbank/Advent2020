with open("Day_03\input.txt") as f:
    content = f.read().splitlines()

position = 0
trees = 0

for c in content:
    if (c[position:position+1]) == '#': trees += 1
    position += 3
    if position >= len(c): position -= len(c)

print(trees)