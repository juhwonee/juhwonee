import sys

input = sys.stdin.readline

N, M = map(int, input().split())

set1 = set()
set2 = set()

for i in range(N):
    N1 = input().strip()
    set1.add(N1)

for i in range(M):
    M1 = input().strip()
    set2.add(M1)

ans = set1 & set2
ans = list(ans)
ans.sort()

print(len(ans))
for i in ans:
    print(i)