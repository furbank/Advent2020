# Read from file into list
with open("Day_01\input.txt") as f:
    content = [int(i) for i in f.read().splitlines()]

r = []

while content:
    a = content.pop()
    r.extend([(x + a, x * a) for x in content if (x + a < 2020)])

print(r)
