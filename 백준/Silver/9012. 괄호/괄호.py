N = int(input())

for _ in range(N):
    S = input()
    stack = []

    for i in S:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack)!=0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')