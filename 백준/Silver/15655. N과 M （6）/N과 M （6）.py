N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []

def solution(start):
    if len(result) == M:
        for i in result:
            print(i, end=' ')
        print()
        return()

    for i in range(start,N):
        if arr[i] not in result:
            result.append(arr[i])
            solution(i+1)
            result.pop()

solution(0)