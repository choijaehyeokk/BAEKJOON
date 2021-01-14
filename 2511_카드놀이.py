import sys

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
A_score: int = 0
B_score: int = 0
for i in range(10):
    if A[i] > B[i] : A_score += 3
    elif A[i] < B[i] : B_score += 3
    else:
        A_score += 1
        B_score += 1

print(A_score, B_score)
if A_score != B_score :
    print('A' if A_score > B_score else 'B')
else:
    if A == B : print('D')
    else:
        for i in range(9, -1, -1):
            if A[i] == B[i] : continue
            else:
                print('A' if A[i] > B[i] else 'B')
                break