import sys
word = sys.stdin.readline().rstrip()
print(1 if word[::-1] == word else 0)
