import sys
N = int(sys.stdin.readline().rstrip())
persons = []
scores = [0] * N
for i in range(N):
    persons.append(list(map(int, sys.stdin.readline().split())))

for i in range(3):
    A = []
    for j in range(N):
        A.append(persons[j][i])

    for k in range(N):
        if A.count(persons[k][i]) > 1: continue
        else:
            scores[k] += persons[k][i]

for i in range(N):
    print(scores[i])