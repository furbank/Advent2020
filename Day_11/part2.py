with open("Day_11\input") as f:
    data = f.read().splitlines()

def IsSeatGood(row, col, maxOcc, plan):
    import numpy as np

    plan = np.array([[col for col in row] for row in plan])

    lenCol = len(plan[0,:])
    lenRow = len(plan[:,0])
    maxCol = lenCol -1
    maxRow = lenRow -1

    print('maxCol:', maxCol)
    print('maxRow:', maxRow)

    print('lenRow:', lenRow)
    print('lenCol:', lenCol)

    print(plan[row, col])

    print('Horizontal')
    print(plan[row, :])

    print('Vertical')
    print(plan[:,col])

    print('Left diagonal')
    lOffset = col - row
    print('Left Offset:', lOffset)
    print(plan.diagonal(lOffset))

    print('Right diagonal')
    rOffset = (lenRow - col) - row
    print('Right Offset:', rOffset)
    print(np.fliplr(plan).diagonal(rOffset))


#IsSeatGood(15, 34, 5, data)
IsSeatGood(94, 83, 5, data)



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
