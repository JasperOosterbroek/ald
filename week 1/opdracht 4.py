import random

"""
description
    Testing of the birtdayParadox on a group of a given size

Parameters
---------
grpsize : int
    The size of the test group

Return
------
    found: int
        percentage of groups with the same birthdays
"""

def birthdayParadox(grpsize):
    found = 0
    samplelst = []
    for x in range(100):
        templst = []
        for y in range(grpsize):
            templst.append(random.randrange(1, 366))
        samplelst.append(templst)

    for x in samplelst:
        seen = []
        for y in x:
            if y not in seen:
                seen.append(y)
            else:
                found = found + 1
                break
    return found


print(birthdayParadox(23))
