import sys
N = list(sys.stdin.readline().rstrip())
F = int(sys.stdin.readline().rstrip())
l = len(N)
result: list = []
for i in range(10):
    for j in range(10):
        N[l-2], N[l-1] = str(i), str(j)
        if int(''.join(N)) % F == 0:
            result.append(str(i) + str(j))
print(result[0])


