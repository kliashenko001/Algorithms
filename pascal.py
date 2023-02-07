from math import *

n = 15
for j in range(n):
    l = []
    for i in range(n):
        if j < i:
            break
        l.append(int(factorial(j) / (factorial(i) * factorial(j - i))))
    print(*l)