N = int(input())

target = [int(input()) for i in range(N)] # 4,3,6,8,7,5,2,1
li = [i for i in range(1, N+1)] # 1,2,3,4,5,6,7,8
stack = []
result = []
idx = 0

for i in li:
    stack.append(i)
    result. append('+')

    while 1:
        if len(stack) == 0:
            break
        if stack[-1] != target[idx]:
            break
        stack.pop()
        result.append('-')
        idx += 1

if idx == N:
    for i in result:
        print(i)
else:
    print('NO')