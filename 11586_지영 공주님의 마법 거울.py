import sys
N = int(sys.stdin.readline().rstrip())
face: list = []
for _ in range(N):
    face.append(list(sys.stdin.readline().rstrip()))
mood = int(sys.stdin.readline().rstrip())

if mood == 1:
    for i in range(N):
        for j in range(N):
            print(face[i][j], end='')
        print()
elif mood == 2:
    for i in range(N):
        face[i] = face[i][::-1]
        for j in range(N):
            print(face[i][j], end='')
        print()
else:
    face = face[::-1]
    for i in range(N):
        for j in range(N):
            print(face[i][j], end='')
        print()