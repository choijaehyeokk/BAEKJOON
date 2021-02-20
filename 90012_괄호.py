import sys
N = int(sys.stdin.readline().rstrip())

for i in range(N):
    ps = list(sys.stdin.readline().rstrip())
    cnt: int = 0
    flag = True
    if ps[0] == ')':
        print('NO')
        continue

    for a in range(len(ps)):
        if ps[a] == '(': cnt += 1
        elif ps[a] == ')': cnt -= 1
        if cnt < 0:
            flag = False
            break

    if flag and cnt == 0:
        print('YES')
    elif flag == False or cnt != 0:
        print('NO')
