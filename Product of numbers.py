n = int(input())
x = [int(input()) for _ in range(n)]
r = int(input())
mark = 'НЕТ'
for i in range(n):
    for j in range(n):
        if j != i:
            if x[i] * x[j] == r:
                mark = 'ДА'

print(mark)
