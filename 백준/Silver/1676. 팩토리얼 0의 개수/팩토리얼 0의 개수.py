import math

N = int(input())
s = str(math.factorial(N))

cnt = 0
for c in reversed(s):
    if c == '0':
        cnt += 1
    else:
        break

print(cnt)
