N, M = map(int, input().split())
result = []

def solution(start):
    if len(result) == M:
        for i in result:
            print(i, end=' ')
        print()

    for i in range(start, N+1):
        if i not in result:
            result.append(i)
            solution(i+1)
            result.pop()

solution(1)