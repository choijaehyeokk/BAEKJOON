import sys
a: list = []
for _ in range(5):
    a.append(int(sys.stdin.readline().rstrip()))
print(int(sum(a)/len(a)))
print(sorted(a)[2])
