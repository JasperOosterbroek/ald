from pprint import pprint
def B(n, k):
    if k <= 0 or n <= 0:
        return 1
    else:
        backLoglist = [[1] + [0] * k for _ in range(n+1)]

        for rowNumb in range(1, n+1):
            for columnNumb in range(1, k+1):
                backLoglist[rowNumb][columnNumb] = backLoglist[rowNumb-1][columnNumb] + backLoglist[rowNumb-1][columnNumb-1]
    return backLoglist[n][k]

n = 20
k = 2
print(B(n, k))
