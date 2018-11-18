"""
description
    A function that extracts the numbers from a string and returns a list of those numbers

Parameters
---------
x : string
    The string that contains the numbers that need to be extracted

Return
------
    lst: list
        A list of integers that have been extracted from the input string
"""

def getNumbers(s):
    lst = list()
    nstart = None
    for count, x in enumerate(s):

        if x.isdigit():
            if nstart is None:
                nstart = count
        else:
            if nstart is not None:
                lst.append(s[nstart: count])
                nstart = None

    if nstart is not None:
        lst.append(s[nstart:len(s)])
    return lst


a = 'een123zin45 6 met-632meerdere+7777getallen1'
print(getNumbers(a))