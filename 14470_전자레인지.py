import sys

A = int(sys.stdin.readline().rstrip()) #첫 줄에는 원래의 고기의 온도 A가 주어진다.
B = int(sys.stdin.readline().rstrip()) #둘째 줄에는 목표 온도 B가 주어진다.
C = int(sys.stdin.readline().rstrip()) #셋째 줄에는 얼어 있는 고기를 1℃ 데우는 데 걸리는 시간 C가 주어진다.
D = int(sys.stdin.readline().rstrip()) #넷째 줄에는 얼어 있는 고기를 해동하는 데 걸리는 시간 D가 주어진다.
E = int(sys.stdin.readline().rstrip()) #다섯째 줄에는 얼어 있지 않은 고기를 1℃ 데우는 데 걸리는 시간 E가 주어진다.

if A < 0 :
    print(abs(A) * C + D + (E * B))
else:
    print((B-A) * E)
