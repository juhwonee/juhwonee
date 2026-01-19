N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for i in range(1, N):
    for j in range(1+i, N):
        for k in range(j+1, N):
            if arr[i]+arr[j]+arr[k] > M:
                continue
            else:
                result = max(result, arr[i]+arr[j]+arr[k])

print(result)