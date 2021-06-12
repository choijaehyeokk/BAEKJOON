import sys

N, M, K = map(int, sys.stdin.readline().split())

numbers = []
tree = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))
tree.append(numbers)

for i in range(1, len(numbers)):
    value = []
    for j in range(len(numbers)-i):
        value.append(tree[i-1][j] + tree[0][j+i])
    tree.append(value)

for _ in range(M+K):
    command = list(map(int, sys.stdin.readline().split(' ')))
    if command[0] == 1:
        index = command[1]-1
        change_value = command[2]

        tree[0][index] = change_value
        for i in range(1, len(numbers)):
            for j in range(len(numbers) -i):
                tree[i][j] = tree[i-1][j] + tree[0][j+i]

    elif command[0] == 2:
        cnt = command[2] - command[1]
        print(tree[cnt][command[1]-1])