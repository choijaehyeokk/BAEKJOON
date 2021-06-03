import sys, collections

N = int(sys.stdin.readline().rstrip())
crane = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
boxes = list(map(int, sys.stdin.readline().split()))
time = 0
crane.sort(reverse=True)
boxes.sort(reverse=True)
#print(queue)
if max(crane) < max(boxes):
    print(-1)
else:
    visited = [False] * M
    box_pos = [0] * N
    counting = 0
    while True:
        if counting == len(boxes):
            break

        for c in range(len(crane)):
            while box_pos[c] < len(boxes):
                if not visited[box_pos[c]] and crane[c] >= boxes[box_pos[c]]:
                    counting +=1
                    visited[box_pos[c]] = True
                    box_pos[c] += 1
                    break
                else:
                    box_pos[c] += 1
        time+=1
    print(time)
