n = int(input())
mult = []
for _ in range(n):
    row = [int(i) for i in input().split()]
    mult.append(row)
s = sum(mult[0])
# print(s)
fl = 'YES'
for i in range(n):
    # print(sum(mult[i]))
    if sum(mult[i]) != s:
        fl = 'NO'
    if fl == 'NO':
        break
md = 0
sd = 0
for i in range(n):
    c = 0
    for j in range(n):
        if fl == 'NO':
            break
        c += mult[j][i]
        md += mult[i][i]
        sd += mult[i][n - i - 1]
        # print(c)
    if c != s:
        fl = 'NO'
if md / n != s or sd / n != s:
    fl = 'NO'
check = []
for i in range(n):
    check += mult[i]
for i in range(1, n * n + 1):
    if i not in check:
        fl = 'NO'

print(fl)


