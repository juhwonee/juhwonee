N, M = map(int, input().split())
result = []

def solution():
    if len(result) == M:
        for i in result:
            print(i, end=' ')
        print()
        return()

    for i in range(1, N+1):
        result.append(i)
        solution()
        result.pop()

solution()