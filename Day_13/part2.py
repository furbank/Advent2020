'''
My knowledge of maths is not up to this, but some googling for a hint brought me to Chinese Remainder Theorem
Explanation here: https://youtu.be/ru7mWZJlRQg

Because I'm lazy and only just (maybe) understand this I found some code to "borrow"
https://rosettacode.org/wiki/Chinese_remainder_theorem

I'm going to take the time to understand this because it's the first python code of any length from examples I've
used and there is probably a lot to learn in it.
'''
with open("Day_13\input") as f:
    data = f.read().splitlines()


# data = ['939', '7,13,x,x,59,x,31,19']
# data = ['x', '17,x,13,19']

target = []
offset = 0

for d in data[1].split(','):
    if d.isnumeric():
        target.append( (offset, int(d)))
    offset += 1

[print(t) for t in target]



