import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

last = arr[-1]
cnt = 1

for i in range(N-1, -1, -1):
    if arr[i] > last:
        cnt += 1
        last = arr[i]
print(cnt)