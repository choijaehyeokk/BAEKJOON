# import sys
# day: int = 0
# d: int = 0
# A, B, V = map(int, sys.stdin.readline().split())
# while d < V :
#     d += A
#     if d >= V: break
#     d -= B
#     day += 1
# print(day+1)

import sys,math
A, B, V = map(int, sys.stdin.readline().split())
d = (V-A)/(A-B)
print(int(math.ceil(d))+1)