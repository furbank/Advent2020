data = [15,12,0,14,3,1]

def NextNumber(hist):
    h = hist.copy()
    if h.count(h[-1]) == 1: return 0

    h.reverse()
    return h[1:].index(h[0]) + 1

while len(data) < 2020:
    data.append(NextNumber(data))

print(data[-1])

