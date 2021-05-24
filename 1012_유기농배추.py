import sys, collections

test_case = int(sys.stdin.readline().rstrip())
def search(X, Y):
    x_pos = [0,0,1,-1]
    y_pos = [1,-1,0,0]
    if visited[X][Y]:
        return 0
    queue = collections.deque([[X,Y]])
    while queue:
        current_node = queue.popleft()
        current_X = current_node[0]
        current_Y = current_node[1]
        if not(visited[current_X][current_Y]):
            visited[current_X][current_Y] = True
            for i in range(4):
                new_X = current_node[0] + x_pos[i]
                new_Y = current_node[1] + y_pos[i]
                if not(visited[new_X][new_Y]) and graph[new_X][new_Y] == 1:
                    queue.append([new_X, new_Y])
    return 1

for _ in range(test_case):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0] * (M+2) for _ in range(N+2)]
    visited = [[False] * (M + 2) for _ in range(N + 2)]
    cnt = 0
    point = []
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[Y+1][X+1] = 1
        point.append((Y+1,X+1))
    for p in point:
        cnt += search(p[0], p [1])
    print(cnt)