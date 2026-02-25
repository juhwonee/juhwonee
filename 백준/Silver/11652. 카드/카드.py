import sys
input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    arr.append(int(input()))
arr.sort()

cnt = 1
max = 0
ans = arr[0]

for i in range(N-1):
    if arr[i] == arr[i+1]:
        cnt += 1
    else:
        if cnt > max:
            max = cnt
            ans = arr[i]
        cnt = 1

if cnt > max:
    ans = arr[N-1]
print(ans)