import sys
N = int(sys.stdin.readline().rstrip())
result: int = 0
i: int = 1
while i <= N:
    i = str(i)
    summary: int = 0
    for j in range(len(i)):
        summary += int(i[j])
    summary += int(i)
    if summary == N: result = i; break
    i = int(i) + 1
print(result)
