import sys
K = int(sys.stdin.readline().rstrip())
# display = ["A"]
# for _ in range(K):
#     result = ""
#     for i in range(len(display)):
#         if display[i] == 'A': display[i] = 'B'
#         elif display[i] == 'B': display[i] = 'BA'
#     for j in range(len(display)):
#         result += display[j]
#     display = list(result)
# print(display.count('A'), display.count('B'))

AB = [1, 0]
for _ in range(K):
    AB[0], AB[1] = AB[1], AB[0]+AB[1]
print(AB[0], AB[1])
