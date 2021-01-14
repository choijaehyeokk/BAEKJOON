import sys

N = int(sys.stdin.readline().rstrip())
result = []
for i in range(N):
    person = list(map(int, sys.stdin.readline().split()))
    count : int  =0
    number : int =0
    for i in range(len(person)):
        if person[i] == person[i-1]:
            count += 1
            number = person[i]
    if count == 3 : result.append(10000 + number*1000)
    elif count == 1: result.append(1000 + number*100)
    else : result.append(max(person)*100)
print(result)
print(max(result))
