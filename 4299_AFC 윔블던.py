x, y = map(int,input().split())

for a in range(x+1, x//2, -1):
    b = x-a
    if a-b == y:
        print(a, b)
        break
    else:
        print(-1)

