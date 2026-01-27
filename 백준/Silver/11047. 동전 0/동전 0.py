import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coins = []
for i in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)

ans = 0
for i in coins:
    ans += K // i
    K = K % i

    if K <= 0:
        break
print(ans)