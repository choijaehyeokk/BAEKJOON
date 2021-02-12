import sys
colors = []
nums = []
result = []

def cal(i: int, A: list)->int:
    if i == 1:
        return max(A) + 900
    elif i == 2:
        for j in range(len(A)):
            if A.count(A[j]) > 1:
                return A[j] + 800
    elif i == 3:
        B = list(set(A))
        if A.count(B[0]) == 2:

            return B[1] * 10 + B[0] + 700
        else:
            return B[0] * 10 + B[1] + 700
    elif i == 4:
        return max(A) + 600
    elif i == 5:
        return max(A) + 500
    elif i == 6:
        for j in range(len(A)):
            if A.count(A[j]) > 1:
                return A[j] + 400
    elif i == 7:
        results = []
        B = list(set(A))
        for b in B:
            if A.count(b) == 1: continue
            elif A.count(b) == 2: results.append(b)
        results = sorted(results)
        return results[0] + results[1] * 10 + 300
    elif i == 8:
        for j in range(len(A)):
            if A.count(A[j]) > 1:
                return A[j] + 200
    elif i == 9:
        return max(A) + 100

for _ in range(5):
    color, num = map(str,sys.stdin.readline().split())
    colors.append(color)
    nums.append(int(num))
cnt_nums = sorted(set(nums))

if len(set(colors)) == 1:
    result.append(4)
    start = cnt_nums[0]
    idx = 0
    for j in range(1, len(cnt_nums)):
        if cnt_nums[j] == (start + 1):
            start = cnt_nums[j]
            idx += 1
        else:
            break
    if idx == 4: result.append(1)

if len(cnt_nums) == 5:
    start = cnt_nums[0]
    idx = 0
    for j in range(1, len(cnt_nums)):
        if cnt_nums[j] == (start + 1):
            start = cnt_nums[j]
            idx += 1
        else:
            break
    if idx == 4: result.append(5)
    else: result.append(9)

elif len(cnt_nums) == 2:
    if nums.count(cnt_nums[0]) == 1 or nums.count(cnt_nums[0]) ==4:
        result.append(2)
    else:
        result.append(3)
elif len(cnt_nums) == 3:
    for n in cnt_nums:
        if nums.count(n) == 1: continue
        elif nums.count(n) == 2: result.append(7)
        elif nums.count(n) == 3: result.append(6)
elif len(cnt_nums) == 4:
    result.append(8)

result = sorted(result)[0]
print(cal(result, nums))