import sys

walks = list(map(int, sys.stdin.readline().split()))
walks = sorted(walks)
print(walks[0]*walks[2])


