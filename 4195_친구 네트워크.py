# import sys
# import collections
#
# def dfs(friends: dict, root: str)->int:
#     queue = collections.deque()
#     queue.append(root)
#     visited = []
#     cnt = 0
#     while queue:
#         current_node = queue.popleft()
#         if current_node not in visited:
#             cnt += 1
#             visited.append(current_node)
#             for x in friends[current_node]:
#                 queue.append(x)
#     return cnt
#
# T = int(sys.stdin.readline().rstrip())
# for _ in range(T):
#     F = int(sys.stdin.readline().rstrip())
#     friend = {}
#     for i in range(F):
#         id1, id2 = sys.stdin.readline().split()
#         root = id1
#         if id1 not in friend:
#             friend[id1] = [id2]
#         else:
#             friend[id1].append(id2)
#
#         if id2 not in friend:
#             friend[id2] = [id1]
#         else:
#             friend[id2].append(id1)
#
#         result = dfs(friend, root)
#         print(result)

import sys
def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p

def union(X, Y):
    x = find(X)
    y = find(Y)

    if x != y:
        parent[y] = x
        network_size[x] += network_size[y]

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    F = int(sys.stdin.readline().rstrip())
    parent = dict()
    network_size = dict()
    for _ in range(F):
        id1, id2 = sys.stdin.readline().split()
        if id1 not in parent:
            parent[id1] = id1
            network_size[id1] = 1
        if id2 not in parent:
            parent[id2] = id2
            network_size[id2] = 1

        union(id1, id2)
        print(network_size[find(id1)])