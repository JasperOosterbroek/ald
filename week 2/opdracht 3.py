"""
naam: Jasper Oosterbroek
studentnummer: 1719848
klas: TI-V2C
docent: Frits Dannenberg
"""


"""
description
    A self-made parenthesis problem checker

Parameters
----------
s : list
    A list to be checked for correctness via the parenthesis problem


Return
------
(none): boolean
    A boolean if the inserted string is correct via the parenthesis problem

"""
def parenthesisProblem(s):
    assert isinstance(s, str), "must be string"
    opening = ['<', '[', '(']
    closing = ['>', ']', ')']
    stack = list()

    for x in s:
        if x not in opening and x not in closing:
            return False
        if x in opening:
            stack.append(x)
        if x in closing:
            if not stack:
                return False
            y = stack.pop()
            if opening.index(y) != closing.index(x):
                return False
    if stack:
        return False

    return True


s = "<<<<"

print(parenthesisProblem(s))
