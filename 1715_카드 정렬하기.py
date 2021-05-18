import sys
import heapq
cards = []
min_heap = []
result = 0
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    heapq.heappush(cards, num)

while len(cards) > 1:
    first, second = heapq.heappop(cards), heapq.heappop(cards)
    value = first + second
    result += value
    heapq.heappush(cards, value)

print(result)
