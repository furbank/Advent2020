with open("Day_11\input") as f:
    data = f.read().splitlines()

def OccupiedNeighbours(row, col, plan):
    import numpy as np

    plan = np.array([[col for col in row] for row in plan])

    maxCol = len(plan[0,:]) -1

    #Slice line of sight out of plan
    #Horizontal
    losH = plan[row, :]

    #Vertical
    losV = plan[:,col]

    #Left diagonal
    lOffset = col - row
    losLD = plan.diagonal(lOffset)

    #Right diagonal
    rOffset = (maxCol - col) -row
    losRD = np.fliplr(plan).diagonal(rOffset)


    los = []
    #flip start slice so they can all be processed the same
    los.append(list(np.flip(losH[:col])))
    los.append(list(losH[col+1:]))
    los.append(list(np.flip(losV[:row])))
    los.append(list(losV[row+1:]))
    if lOffset < 0:
        los.append(list(np.flip(losLD[:row+lOffset])))
        los.append(list(losLD[row+1+lOffset:]))
    else:
        los.append(list(np.flip(losLD[:row])))
        los.append(list(losLD[row+1:]))

    if rOffset < 0:
        los.append(list(np.flip(losRD[:row+rOffset])))
        los.append(list(losRD[row+1+rOffset:]))
    else:
        los.append(list(np.flip(losRD[:row])))
        los.append(list(losRD[row+1:]))

    vis = [[f for f in l if f != '.'] for l in los if l != []]
    return ([v[0] for v in vis if v != []].count('#'))

maxNeighbours = 5
plan = data.copy()
oldPlan = data.copy()

for i in range(1000):

    for r in range(len(data)):
        for c in range(len(data[r])):
            # if c ==9 and r == 7:
            #     print('break')
            if oldPlan[r][c] == 'L' and OccupiedNeighbours(r, c, oldPlan) == 0:
                # Sit Here
                plan[r] = plan[r][:c] + '#' + plan[r][c+1:]

            if oldPlan[r][c] == '#' and OccupiedNeighbours(r, c, oldPlan) >= maxNeighbours:
                # Vacate Here
                plan[r] = plan[r][:c] + 'L' + plan[r][c+1:]

    if oldPlan == plan:
        print('Stabilized on iteration:', i)
        break

    oldPlan = plan.copy()

print('Occupied seats:',sum([p.count('#') for p in plan]))
