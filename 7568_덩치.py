import sys
N = int(sys.stdin.readline().rstrip())
persons = []
result = []
for _ in range(N):
    persons.append(list(map(int ,sys.stdin.readline().split())))

for i in range(N):
    cnt: int = 0
    for j in range(N):
        if persons[i][0] < persons[j][0] and persons[i][1] < persons[j][1]:
            cnt += 1
    result.append(cnt+1)
print(*result)