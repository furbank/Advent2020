# '''
# My knowledge of maths is not up to this, but some googling for a hint brought me to Chinese Remainder Theorem
# Explanation here: https://youtu.be/ru7mWZJlRQg
#
# Because I'm lazy and only just (maybe) understand this I found some code to "borrow"
# https://rosettacode.org/wiki/Chinese_remainder_theorem
#
# Example: Find the smallest positive integer that can be divided by 3,5,7 to give remainders of 1,4,6 respectively.
#
# I'm going to take the time to understand this because it's the first python code of any length from examples I've
# used and there is probably a lot to learn in it.
# '''
from chinese_remainder import chinese_remainder

with open("Day_13\input") as f:
    data = f.read().splitlines()

n = []
a = []
pos = 0

for d in data[1].split(','):
    if d.isnumeric():
        n.append(int(d))
        a.append(int(d) - pos)
    pos += 1

print(n)
print(a)
print()

print(chinese_remainder(n, a))
