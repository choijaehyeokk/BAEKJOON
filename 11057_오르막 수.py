import sys
N = int(sys.stdin.readline().rstrip())
arr = [1 for _ in range(10)]
arr2 = [1 for _ in range(10)]
def numbers(N: int):
   global arr, arr2

   for i in range(N-1):
       arr2[0] = sum(arr)
       for j in range(9):
           arr2[j+1] = arr2[j] - arr[j]
       for k in range(10):
           arr[k] = arr2[k]

   return sum(arr2)
print(numbers(N) % 10007)