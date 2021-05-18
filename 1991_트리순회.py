import sys

def pre_order(root):
    if root == '.':
        return
    print(root , end='')
    pre_order(tree[root][0])
    pre_order(tree[root][1])

def in_order(root):
    if root == '.':
        return
    in_order(tree[root][0])
    print(root, end='')
    in_order(tree[root][1])

def post_order(root):
    if root == '.':
        return
    post_order(tree[root][0])
    post_order(tree[root][1])
    print(root, end='')

tree = {}

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    node, left, right = sys.stdin.readline().split()
    tree[node] = (left,right)

pre_order('A')
print()
in_order('A')
print()
post_order('A')
