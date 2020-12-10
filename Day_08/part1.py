with open("Day_08\input") as f:
    data = f.read().splitlines()

bootInst = [[d[:3], int(d[4:])] for d in data]

def acc(x):
    global acc, currentInst
    acc += x
    currentInst += 1

def nop(x):
    global currentInst
    currentInst += 1

def jmp(x):
    global currentInst
    currentInst += x

inst = {"acc": acc, "nop": nop, "jmp": jmp}

acc = 0
currentInst = 0
execInst = set()

while currentInst not in execInst and currentInst < len(bootInst):
    execInst.add(currentInst)
    inst[bootInst[currentInst][0]](bootInst[currentInst][1])

print(acc)
