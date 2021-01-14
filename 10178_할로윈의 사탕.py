import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    c , v = map(int, sys.stdin.readline().split())
    print('You get {0} piece(s) and your dad gets {1} piece(s).'.format(c//v, c%v))