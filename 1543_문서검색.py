import sys

string = sys.stdin.readline().rstrip()
find_word = sys.stdin.readline().rstrip()

length = len(find_word)
index, result = 0, 0
while index <= len(string):
    if string[index: index + length] == find_word:
        result += 1
        index += length
    else:
        index += 1
print(result)