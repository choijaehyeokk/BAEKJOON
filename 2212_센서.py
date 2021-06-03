import sys

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
sensors_pos = list(map(int, sys.stdin.readline().split()))
sensors_pos.sort()
distance = []
if K >= N:
    print(0)
    sys.exit()
#우선 각 점들의 거리를 구하고 가장 긴 곳 부터 끊어준다.
for i in range(len(sensors_pos)-1):
    distance.append(abs(sensors_pos[i] - sensors_pos[i+1]))
#print(distance)
distance.sort(reverse=True)
for i in range(K-1):
    distance[i] = 0
print(sum(distance))