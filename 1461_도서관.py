import sys, heapq
N, M = map(int,sys.stdin.readline().split())
book_pos = list(map(int, sys.stdin.readline().split()))

large = max(max(book_pos), -min(book_pos))
pos, neg = [],[]
#Max heap으로 우선 순위 큐를 구현한다.
for i in book_pos:
    if i > 0:
        heapq.heappush(pos, -i)
    else:
        heapq.heappush(neg, i)
result = 0
while pos:
    result += -heapq.heappop(pos)
    #M개씩 큰것부터 뽑아냄
    for _ in range(M - 1):
        if pos:
            heapq.heappop(pos)
while neg:
    result += -heapq.heappop(neg)
    for _ in range(M - 1):
        if neg:
            heapq.heappop(neg)

print(result * 2 - large)

