N, M = map(int, input().split())
arr = list(map(int, input().split())) # 9 7 9 1
arr.sort() # 1 7 9 9
result = []

def solution(start):
    if len(result) == M:
        for i in result:
            print(arr[i], end=' ')
        print()
        return()

    prev = 0
    for i in range(start, N):
        if i not in result and arr[i] != prev:
            result.append(i)
            prev = arr[i]

            solution(i+1)
            result.pop()

solution(0)