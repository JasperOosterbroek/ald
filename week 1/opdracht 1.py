"""
naam: Jasper Oosterbroek
studentnummer: 1719848
klas: TI-V2C
docent: Frits Dannenberg
"""

"""
description
    A self made max function

Parameters
---------
a : list
    The list that needs it's max returned

Return
------
    y: int or float
        max value of list as int or float
"""


def mymax(a):
    assert len(a) > 0, "The length of the list must be greater than zero"
    assert all([isinstance(x, (int, float)) for x in a]), "One of the elements is not a float or integer"
    y = a[0]
    for x in a:
        if x > y:
            y = x
    return y


a = [1, 2, 3, 4]
print(mymax(a))  # expected result: 4

a = [1.1, 1.2, 1.3, 1.4]
print(mymax(a))  # expected result: 1.4

a = [1.1, 2, 3.3, 4]
print(mymax(a))  # expected result: 4

a = [-9, -4, -2, -1]
print(mymax(a))  # expected result: -1

# a = [1, "a", 3, 4]
# print(mymax(a))  # expected result: assertion error

# a = []
# print(mymax(a))  # expected result: assertion error
