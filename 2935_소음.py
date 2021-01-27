import sys

A = int(sys.stdin.readline().rstrip())
operand = sys.stdin.readline().rstrip()
B = int(sys.stdin.readline().rstrip())

print(A+B if operand == '+' else A*B)