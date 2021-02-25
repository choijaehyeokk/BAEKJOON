import sys, collections
N = int(sys.stdin.readline().rstrip())
numbers = collections.deque()

for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        numbers.pop()
    else:
        numbers.append(num)
print(sum(numbers))