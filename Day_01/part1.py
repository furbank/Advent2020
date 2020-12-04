# Read from file into list
with open("Day_01\input.txt") as f:
    content = [int(i) for i in f.read().splitlines()]

while content:
    a = content.pop()
    r = [x * a for x in content if (x+a==2020)]
    if r: print(r.pop())

