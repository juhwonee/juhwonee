import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
sum1 = 0
ans = 0
for i in arr:
    sum1 += i
    ans += sum1
print(ans)