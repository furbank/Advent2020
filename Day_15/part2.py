data = [15,12,0,14,3,1]

hist = {}
aTurn = 0

for d in data[:-1]:
    aTurn += 1
    hist[d] = aTurn

aNum = data[-1]
bNum = 0
aTurn += 1

while aTurn < 30000000:
    if aNum in hist:
        bNum = aTurn - hist[aNum]
    else:
        bNum = 0

    hist[aNum] = aTurn
    aTurn += 1
    aNum = bNum

print('On turn {} the number spoken is {}'.format(aTurn, aNum))
