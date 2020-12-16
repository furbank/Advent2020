with open("Day_11\input") as f:
    data = f.read().splitlines()

import numpy as np

a = np.array([[col for col in row] for row in data])

print(a)
print()

row =15
col =34

lenCol = len(a[0,:])
lenRow = len(a[:,0])
maxCol = lenCol -1
maxRow = lenRow -1

print('maxCol:', maxCol)
print('maxRow:', maxRow)

print('lenRow:', lenRow)
print('lenCol:', lenCol)

print(a[row, col])

print('Horizontal')
print(a[row, :])

print('Vertical')
print(a[:,col])

print('Left diagonal')
lOffset = col - row
print('Left Offset:', lOffset)
print(a.diagonal(lOffset))

print('Right diagonal')
rOffset = (lenRow - col) - row
print('Right Offset:', rOffset)
print(np.fliplr(a).diagonal(rOffset))

# def IsSeatGood(row, col, maxOcc, plan):
#     minRow = 0
#     maxRow = len(plan)-1
#     minCol = 0
#     maxCol = len(plan[0])-1

#     #Check n
#     while n != '.':
#         i -= 1
#         print(plan[row + i][col])

#     # Row -1



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
