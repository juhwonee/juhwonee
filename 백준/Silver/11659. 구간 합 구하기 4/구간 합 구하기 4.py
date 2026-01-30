import sys
input = sys.stdin.readline

N, M = map(int,input().split())
nums = list(map(int,input().split()))

sum = 0
sum_arr = [0]
for i in range(N):
    sum += nums[i]
    sum_arr.append(sum)

for _ in range(M):
    a, b = map(int,input().split())
    print(sum_arr[b] - sum_arr[a-1])