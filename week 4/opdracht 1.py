#separate chaining hashing
import random

class SCHash():
    def __init__(self):
        self.hashList = [set() for _ in range(8)]
        self.count = 0
        self.oldFillGrade = 0

    def __repr__(self):
        print("<-------------------->")
        for hashSet in self.hashList:
            if len(hashSet) > 0:
                print(hashSet)
            else:
                print(None)
        print("<-------------------->")
        print("old fill grade : " + str(self.oldFillGrade))
        print("new fill grade : " + str(self.count) + " + " + str(len(self.hashList)) + " = " + str(self.count / len(self.hashList)))
        print("<-------------------->")
    def search(self, e):
        index = hash(e) % len(self.hashList)
        if e in self.hashList[index]:
            return True
        return False

    def insert(self, e):
        index = hash(e) % len(self.hashList)
        if not self.search(e):
            self.hashList[index].add(e)
            self.count += 1

        if self.count / len(self.hashList) > 0.75:
            self.rehash(len(self.hashList)*2)

    def delete(self, e):
        index = hash(e) % len(self.hashList)
        if not self.search(e):
            return False
        else:
            self.hashList[index].remove(e)
            self.count -= 1

    def rehash(self, new_len):
        oldHashList = self.hashList
        self.oldFillGrade = self.count / len(self.hashList)
        self.hashList = [set() for _ in range(new_len)]
        for hashSet in oldHashList:
            for item in hashSet:
                index = hash(item) % new_len
                self.hashList[index].add(item)
        self.__repr__()

hashList = SCHash()

fractionList = list()

for i in range(200):
    fractionList.append(random.randint(1, 99999)/100000)

for i in fractionList:
    hashList.insert(i)

for i in range(100):
    hashList.delete(fractionList[random.randint(0, 200)])

print(hashList)