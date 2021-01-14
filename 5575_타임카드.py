import sys

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
C = list(map(int, sys.stdin.readline().split()))
persons = list()
persons.append(A)
persons.append(B)
persons.append(C)

for person in persons:
    hour : int = person[3] - person[0]
    minute : int = person[4] - person[1]
    seconds : int = person[5] - person[2]

    if seconds < 0 :
        minute -= 1
        seconds += 60
    if minute < 0:
        hour -= 1
        minute += 60
    print(hour, minute, seconds)
