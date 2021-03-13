import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    dictionary = {}
    result = []
    first_key = sys.stdin.readline().split()
    second_key = sys.stdin.readline().split()
    encryption_words = sys.stdin.readline().split()

    for index in range(len(encryption_words)):
        dictionary[second_key[index]] = encryption_words[index]

    for word in first_key:
        result.append(dictionary[word])
    print(*result)