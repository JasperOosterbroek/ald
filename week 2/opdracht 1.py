"""
naam: Jasper Oosterbroek
studentnummer: 1719848
klas: TI-V2C
docent: Frits Dannenberg
"""

def machtv1(a, n): return a ** n

"""
description
    A self-made to the power function that not uses recursion
    
Parameters
----------
a : integer
    The base number
n : integer
    The ammount of times the base number is multiplied by itself

Return
------
count : integer
    The ammount of times the while loop has gone in the if n % 2 == 0 statement
m: integer
    The result of a to the power of n

"""

def machtv3(a, n):
    assert n > 0
    m = 1
    count = 0
    while n > 0:
        if n % 2 == 0:
            a *= a
            n = n / 2
            count += 1
        else:
            m *= a
            n -= 1

    return count, m

print(machtv1(2, 10000))
print(machtv3(2, 10000))