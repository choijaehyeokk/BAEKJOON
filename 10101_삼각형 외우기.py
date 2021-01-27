import sys
angles = []
count : int = 0
for i in range(3):
    angle = int(sys.stdin.readline().rstrip())
    angles.append(angle)

if sum(angles) == 180:
    for i in range(3):
        if angles[i-1] == angles[i]:
            count += 1
    if count == 0:
        print("Scalene")
    elif count == 1:
        print("Isosceles")
    else:
        print("Equilateral")
else:
    print("Error")
