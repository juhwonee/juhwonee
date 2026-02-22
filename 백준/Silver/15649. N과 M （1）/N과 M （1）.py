N, M = map(int, input().split())
result = []

def solution():
    if len(result) == M:
        for i in result:
            print(i, end=' ')
        print()

    for i in range(1, N+1):
        if i not in result:
            result.append(i)
            solution()
            result.pop()

solution()