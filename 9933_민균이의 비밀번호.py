import sys
N = int(sys.stdin.readline().rstrip())
words: list = []
for _ in range(N):
    words.append(sys.stdin.readline().rstrip())

for i in range(len(words)-1):
    for j in range(i, len(words)):
        if words[i] == words[j][::-1]:
            a = len(words[i])
            print(a, words[i][a//2])
            break
