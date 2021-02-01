import sys
N = int(sys.stdin.readline().rstrip())
persons = []
for _ in range(N):
    age, name = map(str, sys.stdin.readline().split())
    persons.append([int(age), name])
persons = sorted(persons, key=lambda x: x[0])

for A in persons:
    print(A[0], A[1])