# Read from file into list
with open("Day_01\input.txt") as f:
    content = [int(i) for i in f.read().splitlines()]

r = []

while content:
    a = content.pop()
    content2 = content.copy()
    while content2:
        b = content2.pop()
        if a + b < 2020:
            r.extend([(x, a, b, x * a * b) for x in content2 if (x + a + b == 2020)])

print(r)
