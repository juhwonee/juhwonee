S = input()
stack = []
ans = 0
ans2 = 1

for i in range(len(S)):
    if S[i] == '(':
        stack.append('(')
        ans2 *= 2

    elif S[i] == '[':
        stack.append('[')
        ans2 *= 3

    elif S[i] == ')':
        if len(stack) == 0 or stack[-1] == '[':
            ans = 0
            break
        elif S[i-1] == '(':
            ans += ans2
        stack.pop()
        ans2 = ans2 // 2

    else:
        if len(stack) == 0 or stack[-1] == '(':
            ans = 0
            break
        elif S[i-1] == '[':
            ans += ans2
        stack.pop()
        ans2 = ans2 // 3

if len(stack) == 0:
    print(ans)
else:
    print(0)