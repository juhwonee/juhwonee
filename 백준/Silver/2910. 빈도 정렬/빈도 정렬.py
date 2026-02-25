import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = list(map(int, input().split()))

cnt = {}
idx = {}
for i in range(N):
    n = arr[i]
    if n not in cnt:
        cnt[n] = 1
        idx[n] = i
    else:
        cnt[n] += 1

nums = []
for i in arr:
    if i not in nums:
        nums.append(i)

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if cnt[nums[i]] < cnt[nums[j]]:
            nums[i], nums[j] = nums[j], nums[i]
        elif cnt[nums[i]] == cnt[nums[j]]:
            if idx[nums[i]] > idx[nums[j]]:
                nums[i], nums[j] = nums[j], nums[i]

for i in nums:
    for _ in range(cnt[i]):
        print(i, end=' ')