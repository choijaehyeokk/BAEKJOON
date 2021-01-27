import sys
while True:
    isosceles: bool = False
    sides = list(map(int, sys.stdin.readline().split()))
    if sides[0]==0 and sides[1]==0 and sides[2]==0: break
    sides = sorted(sides)

    if sides[2] >= sides[0]+sides[1]: print('Invalid')
    elif sides[2] == sides[1] == sides[0]: print('Equilateral')
    else:
        for i in range(3):
            if sides[i-1] == sides[i]: isosceles=True
        print('Isosceles' if isosceles else 'Scalene')
    isosceles = False