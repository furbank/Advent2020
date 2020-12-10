with open("Day_08\input") as f:
    data = f.read().splitlines()

# data = ['nop +0',
# 'acc +1',
# 'jmp +4',
# 'acc +3',
# 'jmp -3',
# 'acc -99',
# 'acc +1',
# 'jmp -4',
# 'acc +6']

data = list(enumerate(data))
bootInst = [[d[0], d[1][:3], int(d[1][4:])] for d in data]

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
    inst[bootInst[currentInst][1]](bootInst[currentInst][2])

print(acc)
