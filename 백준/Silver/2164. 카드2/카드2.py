from collections import deque

N = int(input())
deq = deque(i for i in range(1, N+1))

while(len(deq) > 1):
    deq.popleft()
    q = deq[0]
    deq.popleft()
    deq.append(q)
print(deq[0])