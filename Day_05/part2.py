with open("Day_05\input") as f:
    data = f.read().splitlines()

# convert to row and column id to base10 int
data = [(int(d[:7].replace('B','1').replace('F','0'),2), int(d[7:].replace('R','1').replace('L','0'),2)) for d in data]
data = [d[0]*8+d[1] for d in data]
data.sort()
print (data)