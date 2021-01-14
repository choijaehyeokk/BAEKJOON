import sys
distance = list(map(int, sys.stdin.readline().split()))
count: int = 0
left: int = distance[0]
middle : int = distance[1]
right: int = distance[2]
while True:
    if right - left == 2: break
    if middle - left < right - middle:
        left, middle, right = middle, middle+1, right
        count += 1
    elif middle - left > right - middle:
        left, middle, right = left, middle-1 ,middle
print(count)




