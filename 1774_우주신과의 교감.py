import sys, math

#유클라디안 거리를 구한다.
def dist(point1, point2):
    X = point1[0] - point2[0]
    Y = point1[1] - point2[1]
    return math.sqrt((X*X) + (Y*Y))

#사이클이 생기는지 확인하기 위해서 Union-Find 알고리즘을 적용한다.
def get_parent(parent, n):
    if parent[n] == n:
        return n
    else:
        #재귀적으로 부모를 찾아나간다.
        return get_parent(parent, parent[n])

def union_parent(parent, X, Y):
    X_parent = get_parent(parent,X)
    Y_parent = get_parent(parent,Y)

    #Y의 부모가 X의 부모보다 크다면 X의 부모를 Y의 부모로 갱신한다. (작은 수가 높은 부모로 설정)
    if X_parent < Y_parent:
        parent[Y_parent] = X_parent
    else:
        parent[X_parent] = Y_parent

def find_parent(parent,X,Y):
    X_parent = get_parent(parent,X)
    Y_parent = get_parent(parent,Y)
    #같은 부모라면 사이클이 생기는 것이니까 MST에 넣을 수 없다.
    if X_parent == Y_parent:
        return True
    else:
        return False

N, M = map(int, sys.stdin.readline().split())
points = [] #점들
edges = []#간선들
parent = {}
for _ in range(N):
    X, Y = map(int,sys.stdin.readline().split())
    points.append([X,Y])

for i in range(len(points)-1):
    for j in range(i+1, len(points)):
        edges.append([i+1, j+1, dist(points[i], points[j])])
edges.sort(key=lambda x: x[2]) #거리로 오름차순 정렬
for i in range(1, N+1):
    parent[i] = i #자신의 부모는 바로 자기 자신
for _ in range(M):
    a_X, a_Y = map(int, sys.stdin.readline().split())
    union_parent(parent, a_X, a_Y)

#kruskal 알고리즘 부분
result = 0
for x, y, distance in edges:
    if not find_parent(parent,x,y):
        union_parent(parent,x,y)
        result += distance
print("%0.2f" %result)
