import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)
queue = deque()
queue.append(1)
visited[1] = True
cnt = 0

while len(queue) > 0:
    cur = queue.popleft()

    for next in graph[cur]:
        if not visited[next]:
            visited[next] = True
            queue.append(next)

            cnt += 1

print(cnt)