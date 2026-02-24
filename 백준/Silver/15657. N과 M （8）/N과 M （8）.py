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

    for i in range(start, N):
        result.append(arr[i])
        solution(i)
        result.pop()

solution(0)