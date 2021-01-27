import sys

sang = int(sys.stdin.readline().rstrip())
jung = int(sys.stdin.readline().rstrip())
ha = int(sys.stdin.readline().rstrip())
coke = int(sys.stdin.readline().rstrip())
cider = int(sys.stdin.readline().rstrip())

print(min(sang + coke,
          sang + cider,
          jung + coke,
          jung + cider ,
          ha + coke,
          ha + cider) - 50)


