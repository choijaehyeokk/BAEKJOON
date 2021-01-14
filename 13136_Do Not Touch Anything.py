import sys

R, C, N = map(int, sys.stdin.readline().split())

result : int = 0
R_m = R % N
R = R // N
C_m = C % N
C = C // N

result = R * C
if R_m != 0 and C_m != 0:
    result += (R + C) + 1
elif R_m != 0 and C_m == 0:
    result += C
elif C_m != 0 and R_m == 0:
    result += R

print(result)