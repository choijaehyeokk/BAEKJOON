import sys

N, C =map(int, sys.stdin.readline().split())
x = []
for _ in range(N):
    x.append(int(sys.stdin.readline().rstrip()))
x.sort()

max_dist = x[-1] - x[0]
min_dist = 1
result = 0

while(min_dist <= max_dist):
    mid = (max_dist + min_dist)//2 #거리를 절반씩 계산을 진행함.
    value = x[0] #집의 첫 출발점
    count = 1 #처음 하나는 넣어줌.

    for i in range(len(x)):
        if x[i] >= value + mid:
            count += 1
            value = x[i] #mid 만큼 커버되는 지역에 있으면 공유기를 놓고 지나감

    if count >= C: #지금 놓아봤는데, 원하는 갯수보다 많으면
        min_dist = mid + 1 #최소 길의보다 1큰 걸로 세팅함, 그래야지 mid 가 커져서 count가 작아질 것임. => 그래야 count를 줄여갈 수 있음.
        result = mid
    else:
        max_dist = mid - 1 #원하는 갯수보다 공유기 갯수가 적으면, 중간값보다 1을 작게해서 mid를 줄여나감. => 그래야 count를 늘릴 수 있음

print(result)





