import sys
N = int(sys.stdin.readline().rstrip())
books = {}
name = ''
current_max = 0
for _ in range(N):
    book = sys.stdin.readline().rstrip()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1
books = sorted(books.items(), key= lambda x : x[0])
#print(books)
for k, v in books:
    if current_max < v:
        name = k
        current_max = v
print(name)