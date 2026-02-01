import sys
input = sys.stdin.readline

n = int(input())

dp = [0,1,3,5,11] + [0 for _ in range(1001)]

for i in range(5,n+1):
    dp[i] = (dp[i-1] + 2*dp[i-2])%10007
print(dp[n])