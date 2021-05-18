import sys
class Node:
    def __init__(self, num, left, right):
        self.parent = -1
        self.number = num
        self.left_node = left
        self.right_node = right

def in_order(node, level):
    global level_depth, x

    level_depth = max(level, level_depth)
    if node.left_node != -1:
        in_order(tree[node.left_node], level+1)

    min_level[level] = min(min_level[level],x)
    max_level[level] = max(max_level[level],x)
    x += 1

    if node.right_node != -1:
        in_order(tree[node.right_node], level+1)

N = int(sys.stdin.readline().rstrip())
tree = {}
min_level = [N]
max_level = [0]
level_depth = 1
x,root = 1, -1
for i in range(1, N+1):
    tree[i] = Node(i, -1, -1)
    min_level.append(N)
    max_level.append(0)

for _ in range(N):
    num, left, right = map(int,sys.stdin.readline().split())
    tree[num].left_node = left
    tree[num].right_node = right
    if left != -1:
        tree[left].parent = num
    if right != -1:
        tree[right].parent = num

for i in range(1, N+1):
    if tree[i].parent == -1:
        root = i

in_order(tree[root], 1)

result_level = 1
result_width = max_level[1] - min_level[1] + 1
for i in range(2, level_depth + 1):
    width = max_level[i] - min_level[i] + 1
    if result_width < width:
        result_level = i
        result_width = width
print(result_level, result_width)