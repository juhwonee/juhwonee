import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

stack = deque()
for _ in range(N):
    M = input().split()

    if M[0] == 'push':
        stack.append(M[1])
    elif M[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            p = stack.popleft()
            print(p)
    elif M[0] == 'size':
        print(len(stack))
    elif M[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif M[0] == 'front':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
    elif M[0] == 'back':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])