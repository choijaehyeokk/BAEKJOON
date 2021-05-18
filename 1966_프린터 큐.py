import sys

Testcase = int(sys.stdin.readline().rstrip())

for _ in range(Testcase):
    N, M = map(int, sys.stdin.readline().split())
    numbers = []
    #N 은 문서의 갯수 , M 은 궁금한 문서
    cnt = 0
    priority = list(map(int ,sys.stdin.readline().split()))
    for i in range(len(priority)):
        numbers.append((i, priority[i]))

    while numbers:
        flag = False
        for index in range(len(numbers)):
            if numbers[0][1] < numbers[index][1]:
                flag = True
                break

        if flag:
            pop_number = numbers.pop(0)
            numbers.append(pop_number)
        else:
            pop_number = numbers.pop(0)
            cnt += 1
            if M == pop_number[0]:
                break

    print(cnt)
