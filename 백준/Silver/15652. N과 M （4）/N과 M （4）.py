N, M = map(int, input().split())
result = []

def solution(start):
    if len(result) == M:
        for i in result:
            print(i, end=' ')
        print()
        return()

    for i in range(start, N+1):
        result.append(i)
        solution(i)
        result.pop()

solution(1)