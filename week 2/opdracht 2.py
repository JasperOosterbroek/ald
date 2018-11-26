"""
naam: Jasper Oosterbroek
studentnummer: 1719848
klas: TI-V2C
docent: Frits Dannenberg
"""


"""
description
    A self-made to the power function that not uses recursion

Parameters
----------
parameter-naam1 : parameter-type1
    description1
parameter-naam2 : parameter-type2
    description2

Return
------
return-naam: return-type
    description

"""

class Mystack(list) :
    def __init__(self, *args):
        list.__init__(self, *args)

    def push(self, x):
        self.append(x)

    def peek(self):
        if not self.isEmpty():
            return self[-1]
        return False

    def isEmpty(self):
        return len(self) == 0


test = Mystack()
print(test.peek())
print(test.isEmpty())
test.push(5)
test.push(6)
test.push(7)
test.push(8)
test.push(9)
print(test)
test.pop()
print(test)

print(test.peek())

print(test)
