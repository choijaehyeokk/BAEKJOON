import hashlib
import sys
A = hashlib.sha256(sys.stdin.readline().rstrip().encode())
print(A.hexdigest())