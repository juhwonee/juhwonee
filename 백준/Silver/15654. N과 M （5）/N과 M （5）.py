N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []

def solution():
    if len(result) == M:
        for i in result:
            print(i, end=' ')
        print()
        return()

    for i in range(N):
        if arr[i] not in result:
            result.append(arr[i])
            solution()
            result.pop()

solution()