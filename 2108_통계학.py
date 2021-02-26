import sys
from collections import Counter
N = int(sys.stdin.readline().rstrip())
numbers = []
for i in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))
numbers.sort()
nums = Counter(numbers).most_common()
print(round(sum(numbers) / N))
print(numbers[len(numbers) // 2])
if len(nums) > 1:
    if nums[0][1] == nums[1][1]:
        print(nums[1][0])
    else:
        print(nums[0][0])
else:
    print(nums[0][0])
print(max(numbers) - min(numbers))