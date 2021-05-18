import sys
import heapq

min_heap = []
heapq.heapify(min_heap)
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    command = int(sys.stdin.readline().rstrip())
    if command == 0:
        if not min_heap:
            print(0)
        else:
            print(heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap, command)