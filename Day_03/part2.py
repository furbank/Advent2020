with open("Day_03\input.txt") as f:
    content = f.read().splitlines()

def find_trees_in_path( move_right, move_down):
    position = 0
    trees = 0

    for c in content[::move_down]:
        if (c[position:position+1]) == '#': trees += 1
        position += move_right
        if position >= len(c): position -= len(c)

    return(trees)

num = find_trees_in_path( 1, 1)
num *= find_trees_in_path( 3, 1)
num *= find_trees_in_path( 5, 1)
num *= find_trees_in_path( 7, 1)
num *= find_trees_in_path( 1, 2)

print(num)