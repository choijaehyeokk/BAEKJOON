import sys
mod = 1000000
P = int(mod/10 * 15)
def fibo3(n: int)->int:
    numbers = [0] * (P+1)
    numbers[1] = 1
    cnt: int = 2
    while P != cnt:
        numbers[cnt] = (numbers[cnt-1] + numbers[cnt-2]) % mod
        cnt += 1
    return numbers[n % P]

N = int(sys.stdin.readline().rstrip())
print(fibo3(N))


#이 문제는 피사노 주기(Pisano Period)를 갖는 것을 찾는 문제
#mod = 10^k 일 때, k > 2 라면, 주기는 15 × 10^(k-1)
