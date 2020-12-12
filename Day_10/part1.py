with open("Day_10\input") as f:
    data = f.read().splitlines()

data = [int(d) for d in data]
data.append(0)
data.append(max(data)+ 3)
data.sort()
data = list(enumerate(data))
differences = [b[1]-a[1] for b in data for a in data if b[0] == a[0]+1]

print(len([d for d in differences if d == 1]) * len([d for d in differences if d == 3]))
