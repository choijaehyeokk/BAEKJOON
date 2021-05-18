import sys

N = int(sys.stdin.readline().rstrip())
cnt = 1
stack = []
sign = []

for _ in range(N):
    num = int(sys.stdin.readline().rstrip())

    while cnt <= num:
        stack.append(cnt)
        sign.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        sign.append('-')

if len(stack) == 0:
    for s in sign:
        print(s)
else:
    print('NO')





