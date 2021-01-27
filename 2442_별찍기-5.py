import sys
count = int(sys.stdin.readline().rstrip())
j : int  = 1
for i in range(count):
    print(' '* (count - i -1) + j * '*')
    j += 2