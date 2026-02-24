L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
result = []

def solution(start):
    v = 0
    c = 0
    if len(result) == L:
        for i in result:
            if arr[i] in ['a','e','i','o','u']:
                v += 1
            else:
                c += 1

        if v>=1 and c>=2:
            for i in result:
                print(arr[i], end='')
            print()
        return()

    for i in range(start, C):
        result.append(i)
        solution(i+1)
        result.pop()

solution(0)