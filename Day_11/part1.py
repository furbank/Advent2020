with open("Day_11\input") as f:
    data = f.read().splitlines()

def GetAdjacent(row, col, plan):
    # Return the 8 characters surrounding Row and Col
    # locations outside of the bounds will return as '.'
    # assumes all rows of Plan are the same length.
    minRow = 0
    maxRow = len(plan)-1
    minCol = 0
    maxCol = len(plan[0])-1

    lRow = row -1
    hRow = row +1
    lCol = col -1
    hCol = col +1

    a = b = c = d = f = g = h = i = ''

    if lRow < minRow: a = b = c = '.'
    if hRow > maxRow: g = h = i = '.'
    if lCol < minCol: a = d = g = '.'
    if hCol > maxCol: c = f = i = '.'

    if a != '.': a = plan[lRow][lCol]
    if b != '.': b = plan[lRow][col]
    if c != '.': c = plan[lRow][hCol]
    if d != '.': d = plan[row][lCol]
    if f != '.': f = plan[row][hCol]
    if g != '.': g = plan[hRow][lCol]
    if h != '.': h = plan[hRow][col]
    if i != '.': i = plan[hRow][hCol]

    return a+b+c+d+f+g+h+i

plan = data.copy()
oldPlan = data.copy()

for i in range(100):

    for r in range(len(oldPlan)):
        for c in range(len(oldPlan[r])):
            if oldPlan[r][c] == 'L' and '#' not in GetAdjacent(r, c, oldPlan):
                # Sit Here
                plan[r] = plan[r][:c] + '#' + plan[r][c+1:]

            if oldPlan[r][c] == '#' and GetAdjacent(r, c, oldPlan).count('#') > 3:
                # Vacate Here
                plan[r] = plan[r][:c] + 'L' + plan[r][c+1:]

    if oldPlan == plan:
        print('Stabilized on iteration:', i)
        break

    oldPlan = plan.copy()

print('Occupied seats:',sum([p.count('#') for p in plan]))
