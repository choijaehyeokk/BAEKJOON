from itertools import combinations
import sys

def cal(A, B):
    global team
    #print(A, B)
    A_score, B_score = 0, 0
    for i in range(0, len(A)-1):
        for j in range(i+1, len(A)):
            s_i, s_j = A[i], A[j]
            A_score += stats[s_i][s_j] + stats[s_j][s_i]

    for i in range(0, len(B)-1):
        for j in range(i+1, len(B)):
            s_i, s_j = B[i], B[j]
            B_score += stats[s_i][s_j] + stats[s_j][s_i]
    #print(A_score, B_score)
    return abs(A_score - B_score)

N = int(sys.stdin.readline().rstrip())
stats = [[0]*(N+1)]
numbers = []
teams = []
min_score = sys.maxsize
for i in range(1,N+1):
    stats.append([0] + list(map(int ,sys.stdin.readline().split())))
    numbers.append(i)

for team in list(combinations(numbers, N//2)):
    teams.append(team)

for i in range(len(teams) // 2):
    min_score = min(min_score, cal(teams[i], teams[-i-1]))

print(min_score)