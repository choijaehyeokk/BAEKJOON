import sys,string

def group_words(s: str, A: dict)->int:
    i: int = 0
    while i <= len(s)-1:
        if not A[s[i]]:
            A[s[i]] = True
            for j in range(i+1, len(s)):
                if s[i] == s[j]: i += 1
                if s[i] != s[j]: break
        else:
            return 0
        i += 1
    return 1

N = int(sys.stdin.readline().rstrip())
result: int = 0
for _ in range(N):
    A = {}
    for a in list(string.ascii_lowercase):
        A[a] = False

    word = sys.stdin.readline().rstrip()
    result += group_words(word, A)

print(result)