N = int(input())
ans = 0

for _ in range(N):
    S = input()
    stack = []

    for i in S:
        if len(stack)!=0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        ans += 1
print(ans)