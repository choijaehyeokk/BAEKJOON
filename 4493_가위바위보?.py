import sys

test_case = int(sys.stdin.readline().rstrip())

for i in range(test_case):
    count = int(sys.stdin.readline().rstrip())
    result: int = 0
    for j in range(count):
        N, M = map(str, sys.stdin.readline().split())
        if N == M: continue
        else:
            if (N == 'R' and M == 'P') or (N ==  'S' and M=='R') or (N == 'P' and M == 'S'): result+=1
            else: result-=1
    if result == 0: print('TIE')
    else: print('Player 2' if result > 0 else 'Player 1')
