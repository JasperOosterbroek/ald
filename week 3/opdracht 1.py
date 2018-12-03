from itertools import permutations
def check(a,i): # ga na of i aan a toegevoegd kan worden
    n = len(a)
    return not (i in a or
                    # niet in dezelfde kolom
                i+n in [a[j]+j for j in range(n)] or
                    # niet op dezelfde diagonaal
                i-n in [a[j]-j for j in range(n)])
                    # niet op dezelfde diagonaal


def rsearch(N):
    global a
    for i in range(N):
        if check(a,i):
            a.append(i)
            if len(a) == N:
                print(a) # geschikte a gevonden
            else:
                if rsearch(N):
                    return True
            del a[-1] # verwijder laatste element
    return False


a = []
rsearch(8)


