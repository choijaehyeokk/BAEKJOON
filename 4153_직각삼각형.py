import sys, math

while True:
    sides = list(map(int, sys.stdin.readline().split()))
    if sides[0] == 0 and sides[1] == 0 and sides[2] == 0: break
    sides = sorted(sides)
    if sides[2] == math.sqrt(pow(sides[0],2) + pow(sides[1], 2)): print('right')
    else: print('wrong')

