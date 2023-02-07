n = 3
result = []

for _ in range(n):
    result.append(list(range(1, n + 1)))

print(*result, sep='\n')