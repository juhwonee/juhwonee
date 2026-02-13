s = input()
ans = 0
stack = []

for i in range(len(s)):
    if s[i] == '(':
        if s[i+1] == ')':
            ans += len(stack)
        else:
            stack.append(s[i])
            ans += 1

    else:
        if len(stack) != 0 and s[i-1] != '(':
            stack.pop()

print(ans)