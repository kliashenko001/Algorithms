xy = input()
x = '87654321'.index(xy[1])
y = 'abcdefgh'.index(xy[0])
m = [['.' for i in range(8)] for j in range(8)]
m[x][y] = 'N'
#print(x, y)
#print(*m[2])
for i in range(8):
    for j in range(8):
        if (i - x) ** 2 + (j - y) ** 2 == 5:
            m[i][j] = '*'
for i in range(8):
    print(*m[i], end = ' ')
    print()