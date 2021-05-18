import sys
N, M = map(int ,sys.stdin.readline().split())
tree_heights = sorted(list(map(int ,sys.stdin.readline().split())), reverse=True)
max_height = tree_heights[0]
for height in range(max_height, -1, -1):
    dp = [0 for _ in range(N + 1)]
    for index in range(len(tree_heights)):
        h = tree_heights[index] - height
        if h > 0:
            dp[index] = h
        else: break
    if sum(dp) == M:
        print(height)
        break