import sys
N, M = map(int ,sys.stdin.readline().split())
target: int = 0
if N == 1:
    print(1)
elif N == 2:
    if M >= 7 : print(4)
    elif M >= 5 and M <=6: print(3)
    elif M >= 3 and M <=4: print(2)
    else: print(1)
elif N >= 3 and M < 7:
    print(min(4, M))
else:
    print(M-2)
