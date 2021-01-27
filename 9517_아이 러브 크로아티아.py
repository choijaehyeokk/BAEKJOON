import sys

person = int(sys.stdin.readline().rstrip())
questions = int(sys.stdin.readline().rstrip())
total_time = 210
sum_time = 0
for i in range(questions):
    TZ = sys.stdin.readline().split()
    time, Z = int(TZ[0]), TZ[1]
    sum_time += time
    if sum_time >=  total_time:
        print(person)
        break
    if Z == 'P' or Z == 'N': continue
    elif Z == 'T':
        person += 1
        if person > 8: person %= 8

