"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
from collections import Counter

# Score categories.
# Change the values as you see fit.
YACHT = lambda x: 50 if len(set(x)) == 1 else 0
ONES = lambda x: x.count(1)*1
TWOS = lambda x: x.count(2)*2
THREES = lambda x: x.count(3)*3
FOURS = lambda x: x.count(4)*4
FIVES = lambda x: x.count(5)*5
SIXES = lambda x: x.count(6)*6
FULL_HOUSE = lambda x: sum(x) if 3 in Counter(x).values() and 2 in Counter(x).values() else 0
FOUR_OF_A_KIND = lambda x: sum([k for k,v in Counter(x).items() if v >= 4]) * 4
LITTLE_STRAIGHT = lambda x: 30 if all([i+1 in x for i in range(5)]) else 0
BIG_STRAIGHT = lambda x: 30 if all([i+1 in x for i in range(1,6)]) else 0
CHOICE = sum

def score(dice, category):
    return category(dice)
