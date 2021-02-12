import sys
w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline().rstrip())
X = (p + t) % (w * 2)
Y = (q + t) % (h * 2)
if X > w: X = (2*w)-X
if Y > h: Y = (2*h)-Y
print(X, Y)

# x = [1, -1]
# y = [1, -1]
# dir_x = x[0]
# dir_y = y[0]
# while t != 0:
#     if w == p and h == q:
#         dir_x *= x[1]
#         dir_y *= y[1]
#         p += dir_x
#         q += dir_y
#     elif p == 0 and q == 0:
#         dir_x = x[0]
#         dir_y = y[0]
#         p += dir_x
#         q += dir_y
#     elif p == w and h == 0:
#         dir_x = x[1]
#         dir_y = y[0]
#         p += dir_x
#         q += dir_y
#     elif p == 0 and h == w:
#         dir_x = x[0]
#         dir_y = y[1]
#         p += dir_x
#         q += dir_y
#     else:
#         if w != p and h == q: #위
#             dir_y = y[1]
#             p += dir_x
#             q += dir_y
#         elif w == p and h != q: #오른쪽
#             dir_x = x[1]
#             p += dir_x
#             q += dir_y
#         elif p == 0 and q != 0: #왼쪽
#             dir_x = x[0]
#             p += dir_x
#             q += dir_y
#         elif p != 0 and q == 0: #아래
#             dir_y = y[0]
#             p += dir_x
#             q += dir_y
#         else: #아닌 경우
#             p += dir_x
#             q += dir_y
#
# print(p, q)
