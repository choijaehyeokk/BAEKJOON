import sys
N = int(sys.stdin.readline().rstrip())
words = []
new_list = []
for _ in range(N):
    words.append(sys.stdin.readline().rstrip())

for v in words:
    if v not in new_list:
        new_list.append(v)
new_list.sort()
new_list.sort(key=len)
for v in new_list:
    print(v)

'''other code by lambda
for i in range(n):
    word = str(sys.stdin.readline().rstrip())
    word_len = len(word)
    new_list.append((word, word_len))

new_list = list(set(new_list))
new_list.sort(key = lambda word:(word[1], word[0]))
#lambda의 key 로 들어가는 부분은 파라미터하나를 설정하고, 순서대로 (0,1,...) 써주면 된다.
'''