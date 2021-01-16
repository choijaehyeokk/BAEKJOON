import sys
N = int(sys.stdin.readline().rstrip())
result: int = 0
for i in range(1, N+1):
    for j in range(i+1):
        result += j
    result += i*(i+1)
print(result)