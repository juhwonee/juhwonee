import sys
input = sys.stdin.readline
from collections import deque

queue = deque()
N = int(input())

for _ in range(N):
    M = input().split()

    if M[0] == 'push_front':
        queue.appendleft((M[1]))

    elif M[0] == 'push_back':
        queue.append(M[1])

    elif M[0] == 'pop_front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()

    elif M[0] == 'pop_back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
            queue.pop()

    elif M[0] == 'size':
        print(len(queue))

    elif M[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif M[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])

    elif M[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])