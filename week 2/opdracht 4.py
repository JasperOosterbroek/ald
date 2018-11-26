"""
naam: Jasper Oosterbroek
studentnummer: 1719848
klas: TI-V2C
docent: Frits Dannenberg
"""


"""
description
    A self-made integer to binary converter using recursive

Parameters
----------
n : integer
    An integer to be converted to binary

Return
------
(None): string
    The binary string from the converted integer

"""
def mybin(n):
    assert n >= 0, "given int should be greater than 0"
    assert isinstance(n, int), "N must be an integer"

    if n == 0:
        return '0b0'
    elif n == 1:
        return '0b1'
    else:
        return mybin(n//2) + str(n%2)

x = 100
print(mybin(x))
