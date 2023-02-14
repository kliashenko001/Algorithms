n, m = [int(i) for i in input().split()]
nm = 0
lst = [[j for j in range(m)] for i in range(n)]
for q in range(n*m):
    for i in range(n):
        for j in range(m):
            if i+j == q:
                nm += 1
                lst[i][j] = nm
for i in range(n):
    print(*lst[i], end = ' ')
    print()