import sys
C = int(sys.stdin.readline().rstrip())
for _ in range(C):
    scores = list(map(int, sys.stdin.readline().split()))
    N = scores[0]
    mean = sum(scores[1:])/N
    students: int = 0
    for i in range(1, N+1):
        if scores[i] > mean: students += 1
    print('%0.3f%%' %((students/N)*100))