import sys
testcase = int(sys.stdin.readline().rstrip())

def cal(sentence, n):
    #n == N 까지 도달하게 된다면 식을 계산하고 0이라면 출력해냄
    if n==N:
        sentence += str(n)
        if eval(sentence.replace(" ", "")) == 0:
            print(sentence)
        return

    cal(sentence + str(n) + ' ', n + 1)
    cal(sentence + str(n) + '+', n + 1)
    cal(sentence + str(n) + '-', n + 1)


for _ in range(testcase):
    N = int(sys.stdin.readline().rstrip())
    cal('',1)
    print()