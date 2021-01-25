import sys
PC_rooms = [False]*101
N = sys.stdin.readline().rstrip()
persons = list(map(int, sys.stdin.readline().split()))
result: int = 0
for i in persons:
    if PC_rooms[i] == False:
        PC_rooms[i] = True
    else:
        result+=1
print(result)
