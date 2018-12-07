import random


def findDupeHash(samplesize):
    hashDict = dict()
    for i in range(samplesize):
        randV = random.randint(1, 9999999999999999) / 10000000000000000
        randVHash = hash(randV)
        if randVHash in hashDict:
            return hashDict[randVHash], randV, randVHash
        else:
            hashDict[randVHash] = randV


print(findDupeHash(2**16))
