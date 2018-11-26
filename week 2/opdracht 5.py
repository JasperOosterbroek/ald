def swap(a,i,j):
    a[i],a[j] = a[j],a[i]


import random

def qsort(a,low=0,high=-1):
    global count

    if high == -1:
        high = len(a) -1
    if low < high:
        swap(a,low, random.randint(low,high))
        m = low
        for j in range(low+1,high+1):
            count += 1
            if a[j] < a[low]:
                m += 1
                swap(a,m,j)
        swap(a,low,m)
        if m > 0:
            qsort(a,low,m-1)
        qsort(a,m+1,high)


def worstCaseQsort(a, low=0, high=-1):
    global count

    if high == -1:
        high = len(a) -1
    if low < high:
        swap(a, low, a.index(min(a[low:high])))
        m = low
        for j in range(low+1, high+1):
            count += 1
            if a[j] < a[low]:
                m += 1
                swap(a, m, j)
        swap(a, low, m)
        if m > 0:
            worstCaseQsort(a, low, m-1)
        worstCaseQsort(a, m+1, high)


count = 0
test = random.sample(range(1000), 1000)

print(test)
qsort(test)
print(test) # 10708
print(count)

count = 0

test = random.sample(range(1000), 1000)# 10'000 is te veel voor recusrion depth
print(test)
worstCaseQsort(test)
print(test) # 498517
print(count)