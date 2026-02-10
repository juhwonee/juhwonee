import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
num = list(map(int, input().split()))

dq = deque()
for i in range(N):
    dq.append(i+1)

cnt = 0
for i in num:
    idx = dq.index(i)
    while True:
        if dq[0] == i:
            dq.popleft()
            break

        else:
            if idx <= len(dq)/2:
                temp = dq.popleft()
                dq.append(temp)
                cnt += 1
            else:
                temp = dq.pop()
                dq.appendleft(temp)
                cnt += 1
print(cnt)