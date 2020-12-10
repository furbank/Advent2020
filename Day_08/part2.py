with open("Day_08\input") as f:
    data = f.read().splitlines()

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
currentInst = 0 # enumerator of current instruction
execInst = set() # set of instructions already executed in this iteration


for bi in [bi for bi in bootInst if bi[1] != 'acc']:
    acc = 0
    currentInst = 0
    execInst.clear()

    while currentInst not in execInst and currentInst < len(bootInst):
        execInst.add(currentInst)

        if bi[0] == bootInst[currentInst][0]:
            if bootInst[currentInst][1] == 'jmp':
                inst['nop'](bootInst[currentInst][2])
            else:
                inst['jmp'](bootInst[currentInst][2])

        else:
            inst[bootInst[currentInst][1]](bootInst[currentInst][2])

    if currentInst == len(bootInst):
        print('Reached end of boot instructions. Altered Instruction: ' + str(bi[0]))
        print('Accumulator =' + str(acc))
        break
