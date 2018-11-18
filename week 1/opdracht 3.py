"""
description
    A function that returns the prime values until the given limit

Parameters
---------
n : integer
    The integer is the max value of the prime lookup

Return
------
    lst: list
        A list containing all the prime numbers until the given limit
"""
def sieveOfEratosthenes(n):
    trueList = [True] * n
    trueList[0] = False
    trueList[1] = False
    for cnt, x in enumerate(trueList):
        if x is True:
            for y in range(cnt * cnt, n, cnt):
                trueList[y] = False
    lst = list()
    for cnt, x in enumerate(trueList):
        if x is True:
            lst.append(cnt)
    return lst


limit = 1000
print(sieveOfEratosthenes(limit))