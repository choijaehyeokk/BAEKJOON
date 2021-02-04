import sys
N, K = map(int, sys.stdin.readline().split())
country = []
for _ in range(N):
    country.append(list(map(int, sys.stdin.readline().split())))

country = sorted(country, key=lambda x:(x[1],x[2],x[3]), reverse=True)
idx = 1
for i in range(len(country)):
    if country[i][0] == K:
        for j in range(i+1):
            if country[j][1:] == country[i][1:]:
                continue
            else:
                idx += 1
        break

print(idx)

