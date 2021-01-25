import sys
N = int(sys.stdin.readline().rstrip())
room: list = []
for _ in range(N):
    room.append(sys.stdin.readline().rstrip())

a, b = 0, 0
for i in room:
    width = i.split('X')
    for w in width:
        if len(w) >= 2: a+=1
for j in range(N):
    height: str = ""
    for i in room:
        height += i[j]
    height = height.split('X')
    for h in height:
        if len(h) >= 2: b+=1
print(a, b)

