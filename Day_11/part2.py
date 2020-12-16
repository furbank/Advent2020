with open("Day_11\input") as f:
    data = f.read().splitlines()

def IsSeatGood(row, col, maxOcc, plan):
    import numpy as np

    plan = np.array([[col for col in row] for row in plan])

    occupied = 0
    lenCol = len(plan[0,:])
    lenRow = len(plan[:,0])
    maxCol = lenCol -1
    maxRow = lenRow -1

    #Slice line of sight out of plan
    #Horizontal
    losH = plan[row, :]

    #Vertical
    losV = plan[:,col]

    #Left diagonal
    lOffset = col - row
    losLD = plan.diagonal(lOffset)

    #Right diagonal
    rOffset = (lenRow - col) - row
    losRD = np.fliplr(plan).diagonal(rOffset)

    los = []
    #flip start slice so they can all be processed the same
    los.append(list(np.flip(losH[:col])))
    los.append(list(losH[col+1:]))
    los.append(list(np.flip(losV[:row])))
    los.append(list(losV[row+1:]))
    los.append(list(np.flip(losLD[:col])))
    los.append(list(losLD[col+1:]))
    los.append(list(np.flip(losRD[:row])))
    los.append(list(losRD[row+1:]))

    vis = [[f for f in l if f != '.'] for l in los if l != []]
    return ([v[0] for v in vis if v != []].count('#')) < maxOcc

print(IsSeatGood(10, 96, 5, data))

# plan = data.copy()
# oldPlan = data.copy()

# for i in range(100):

    # for r in range(len(oldPlan)):
        # for c in range(len(oldPlan[r])):
            # if oldPlan[r][c] == 'L' and '#' not in GetAdjacent(r, c, oldPlan):
                # # Sit Here
                # plan[r] = plan[r][:c] + '#' + plan[r][c+1:]

            # if oldPlan[r][c] == '#' and GetAdjacent(r, c, oldPlan).count('#') > 3:
                # # Vacate Here
                # plan[r] = plan[r][:c] + 'L' + plan[r][c+1:]

    # if oldPlan == plan:
        # print('Stabilized on iteration:', i)
        # break

    # oldPlan = plan.copy()

# print('Occupied seats:',sum([p.count('#') for p in plan]))
