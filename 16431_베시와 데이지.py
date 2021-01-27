import sys

B_x, B_y = map(int, sys.stdin.readline().split())
D_x, D_y = map(int, sys.stdin.readline().split())
J_x, J_y = map(int, sys.stdin.readline().split())

Daisy_d = abs(J_x - D_x) + abs(J_y - D_y)
Bessie_d = max(abs(J_x - B_x), abs(J_y - B_y))

if Daisy_d > Bessie_d:
    print("bessie")
elif Bessie_d > Daisy_d:
    print("daisy")
else:
    print("tie")