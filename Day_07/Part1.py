with open("Day_07\input") as f:
    rules = f.read().splitlines()

myBag = 'shiny gold'

rules = [r.split('contain ') for r in rules]
check = [r for r in rules if myBag in r[0]]
rules.remove(check[0])

final = []
while check:
    c = check.pop()
    found = ([r for r in rules if c[0][:-5] in r[1]])

    for f in found:
        rules.remove(f)
        check.append(f)
        final.append(f)
print(len(final))
