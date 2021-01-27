import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())
E = int(sys.stdin.readline().rstrip())
F = int(sys.stdin.readline().rstrip())

science = sorted([A,B,C,D])
history = sorted([E,F])

print(science[1]+science[2]+science[3]+history[1])


