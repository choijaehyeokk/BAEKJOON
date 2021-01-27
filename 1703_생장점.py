import sys

while True:
    tree = list(map(int, sys.stdin.readline().split()))
    if tree[0] == 0 : break
    leaf : int = 1
    year = tree[0]

    for i in range(1, year*2 + 1, 2):
        leaf = (leaf * tree[i]) - tree[i+1]

    print(leaf)

