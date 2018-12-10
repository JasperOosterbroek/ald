from pprint import pprint
def F(n):
    if n > 10000:
        return False
    else:
        m = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
        mc = len(m)
        n += 1
        a = [[0] * n for _ in range(mc)]

        for i in range(mc):
            for j in range(n):
                if j == 0 and i == 0:
                    a[i][j] == 0
                elif j == 0 or i == 0:
                    a[i][j] = 1
                else:
                    if j >= m[i]:
                        a[i][j] = a[i-1][j] + a[i][j-m[i]]
                    elif j < m[i]:
                        a[i][j] = a[i-1][j]
    pprint(a)
    return a[mc-1][n-1]


print(F(200))
