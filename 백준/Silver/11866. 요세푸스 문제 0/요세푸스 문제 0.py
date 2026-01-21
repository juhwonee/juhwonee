import sys

input = sys.stdin.readline
N, K = map(int, input().split())

stack = [i for i in range(1,N+1)]
result = []
idx = 0

while len(stack) > 0:
    idx += K-1
    if idx >= len(stack):
        idx = idx % len(stack)
    result.append(stack.pop(idx))

print('<', end="")
for i in range(N-1):
    print(result[i], end=", ")
print(result[-1], end="")
print('>', end="")