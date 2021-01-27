import sys

S = list(map(int, list(sys.stdin.readline().split())))
T = list(map(int, list(sys.stdin.readline().split())))

if sum(S) == sum(T) :
    print(sum(S))
else :
    print(max(sum(S),sum(T)))

