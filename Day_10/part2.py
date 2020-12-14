with open("Day_10\input") as f:
    data = f.read().splitlines()

# data = [ '16', '10', '15', '5', '1', '11', '7', '19', '6', '12', '4']
# data = ['28','33','18','42','31','14','46','20','48','47','24','23','49','45','19','38','39','11','1','32','25','35','8','17','7','9','4','2','34','10','3']

data = [int(d) for d in data]
data.append(0)
data.append(max(data)+ 3)
data.sort()

#tried to brute force this but it going to take too long
# kept the code as it works and was useful to check results from smaller test sets

#finished = []
#check = [[0]]
# print(data)
# while check:
#     c = check.pop()

#     match = [d for d in data if d > c[-1] and d <= c[-1]+3]

#     if match == []:
#         #[print(c)]
#         finished.append(c)
#     else:
#         for m in match:
#             d = c.copy()
#             d.append(m)
#             d.sort
#             check.append(d)


# print()
# print('total', len(finished))
# print('--------------')

paths = []
check = data.copy()
check = list(enumerate(check))

for c in check:
    match = [d for d in data if d < c[1] and d >= c[1]-3]
    paths.append([c[0], c[1], len(match)])


paths[0].append(1)
for p in paths[1:]:
    if p[2] == 1:
        paths[p[0]].append(paths[p[0]-1][3])
    else:
        paths[p[0]].append(sum([a[3] for a in paths[p[0]-p[2]:p[0]]]))

print('total =', paths[-1][3])


# This is a bit of a mess and could probably be cleaned up, but at the moment I'm tired and just happy it works :)
# I really struggled with this one and needed a hint
# Hint: The number of paths to get to this adapter from the start is equal to the sum of the number of paths to get from the previous adapter to this one.
# from https://dev.to/sleeplessbyte/comment/194fe
