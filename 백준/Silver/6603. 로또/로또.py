while True:
    test = list(map(int, input().split()))
    if test[0] == 0:
        break
    size = test[0]
    arr = test[1:]
    result = []

    def solution(start):
        if len(result) == 6:
            for i in result:
                print(arr[i], end=' ')
            print()
            return ()

        for i in range(start, size):
            result.append(i)
            solution(i+1)
            result.pop()

    solution(0)
    print()